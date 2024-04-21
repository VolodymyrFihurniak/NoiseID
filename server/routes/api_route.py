from fastapi import APIRouter
from psycopg2 import pool

from app.sql_manager import SQLManager
from entities.config import Config
from routes import BaseRoute
from utils.logger import Logger


class ApiRoute(BaseRoute):
	def __init__(
		self,
		router: APIRouter,
		name: str,
		config: Config,
		db_pool: pool,
		sql_manager: SQLManager,
		logging: Logger,
	) -> None:
		super().__init__(router, name, config, db_pool, sql_manager, logging)

	def configure_routes(self):
		api_uri = '/api'

		@self.router.get(f'{api_uri}/info')
		async def api_info():
			"""
			Get the version of the API
			"""
			return {'message': {'version': '0.0.1'}}

		return self.router
