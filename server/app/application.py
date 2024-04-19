from collections import OrderedDict

from dotenv import dotenv_values
from fastapi import APIRouter, FastAPI
from uvicorn import run as server_run
from yaml import Loader, load

from app.sql_manager import SQLManager
from entities.config import Config
from routes import ApiRoute, AuthRoute
from utils.logger import Logger


class App:
	app: FastAPI = None
	config_env: OrderedDict = {}
	config_yaml: dict = {}
	config: Config = None
	sql_manager: SQLManager = None
	logging: Logger = None
	routes: APIRouter = []

	def __init__(self) -> None:
		self.app = FastAPI()
		self.config_env = dotenv_values('configs/.env')
		with open('configs/config.yaml', encoding='utf-8') as file:
			self.config_yaml = load(file, Loader=Loader)
		self.config = Config(self.config_env, self.config_yaml)
		self.logging = Logger(self.config)
		self.sql_manager = SQLManager(self.logging)
		self.router = APIRouter()

	def setup(self):
		self.sql_manager.set_up()
		self.routes.append(
			ApiRoute(
				self.router,
				'api',
				self.config,
				None,
				self.sql_manager,
				self.logging,
			)
		)
		self.routes.append(
			AuthRoute(
				self.router,
				'auth',
				self.config,
				None,
				self.sql_manager,
				self.logging,
			)
		)
		self.app.include_router(self.router)

	def on_startup(self):
		if self.config.app.use_https:
			ssl_keyfile = None
			ssl_certfile = None
			with open(self.config.app.ssl_key_path, 'rb') as file:
				ssl_keyfile = file.read()
			with open(self.config.app.ssl_cert_path, 'rb') as file:
				ssl_certfile = file.read()
			server_run(
				self.app,
				host=self.config.app.host,
				port=self.config.app.port,
				log_config=None,
				log_level='info',
				ssl_keyfile=ssl_keyfile,
				ssl_certfile=ssl_certfile,
			)
		else:
			server_run(
				self.app,
				host=self.config.app.host,
				port=self.config.app.port,
				log_config=None,
				log_level='info',
			)