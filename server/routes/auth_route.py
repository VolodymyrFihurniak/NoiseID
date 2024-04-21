from fastapi import APIRouter, Depends, File, UploadFile
from psycopg2 import pool

from controllers.auth_controller import AuthController
from entities.config import Config
from models.authentification import Authentification
from routes import BaseRoute


class AuthRoute(BaseRoute):
	def __init__(
		self,
		router: APIRouter,
		name: str,
		config: Config,
		db_pool: pool,
		sql_manager,
		logging,
	) -> None:
		super().__init__(router, name, config, db_pool, sql_manager, logging)

	def configure_routes(self):
		auth_uri = '/api/auth'
		auth_controller = AuthController(
			self.config, self.db_pool, self.sql_manager, self.logging
		)

		@self.router.post(f'{auth_uri}/registration')
		async def auth_registration(
			user: Authentification = Depends(), stream: UploadFile = File(...)
		):
			"""
			Register a new user
			"""
			data = await stream.read()
			return auth_controller.register(user, data)

		@self.router.post(f'{auth_uri}/login')
		async def auth_login(
			user: Authentification = Depends(), stream: UploadFile = File(...)
		):
			"""
			Login a user
			"""
			data = await stream.read()
			return auth_controller.login(user, data)

		return self.router
