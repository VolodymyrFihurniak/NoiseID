import json

from fastapi import UploadFile
from psycopg2 import pool

from app.sql_manager import SQLManager
from business.auth_worker import AuthWorker
from controllers import BaseController
from data.auth_repository import AuthRepository
from entities.config import Config
from mappers.user_mapper import UserMapper
from models.authentification import Authentification
from utils.logger import Logger


class AuthController(BaseController):
	def __init__(
		self,
		config: Config,
		db_pool: pool,
		sql_manager: SQLManager,
		logging: Logger,
	) -> None:
		super().__init__(config, db_pool, sql_manager, logging)
		self.logging.server.info('AuthController initialized')

	def build_auth_worker(self) -> AuthWorker:
		return AuthWorker(
			AuthRepository(self.db_pool, self.sql_manager, self.logging)
		)

	def register(
		self, user: Authentification, data: UploadFile
	) -> json.JSONEncoder:
		auth_worker = self.build_auth_worker()
		build_user = UserMapper().to_dto(user, data)
		return auth_worker.register(build_user)

	def login(
		self, user: Authentification, data: UploadFile
	) -> json.JSONEncoder:
		auth_worker = self.build_auth_worker()
		build_user = UserMapper().to_dto(user, data)
		return auth_worker.process_login(build_user)
