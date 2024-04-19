from fastapi import APIRouter, Depends, File, UploadFile

from models.authentification import Authentification
from routes.base_route import BaseRoute


class AuthRoute(BaseRoute):
	def __init__(
		self,
		router: APIRouter,
		name: str,
		config,
		db,
		sql_manager,
		logging,
	) -> None:
		super().__init__(router, name, config, db, sql_manager, logging)

	def configure_routes(self):
		auth_uri = '/api/auth'
		auth_controller = None

		@self.router.post(f'{auth_uri}/registration')
		async def auth_registration():
			"""
			Register a new user
			"""
			return {'message': 'registration'}

		@self.router.post(f'{auth_uri}/login')
		async def auth_login(
			user: Authentification = Depends(), stream: UploadFile = File(...)
		):
			"""
			Login a user
			"""
			data = await stream.read()
			return {'message': 'login'}

		return self.router
