from abc import ABC, abstractmethod

from fastapi import APIRouter

from app.sql_manager import SQLManager
from entities.config import Config
from utils.logger import Logger


class BaseRoute(ABC):
	def __init__(
		self,
		router: APIRouter,
		name: str,
		config: Config,
		db,
		sql_manager: SQLManager,
		logging: Logger,
	) -> None:
		self.router = router
		self.name = name
		self.config = config
		self.db = db
		self.sql_manager = sql_manager
		self.logging = logging
		self.configure_routes()
		self.logging.server.info(f'{self.name.capitalize()} route configured')

	def get_name(self) -> str:
		return self.name

	@abstractmethod
	def configure_routes(self) -> APIRouter:
		pass
