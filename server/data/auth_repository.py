from typing import Annotated

from psycopg2 import pool

from app.sql_manager import SQLManager
from dtos.user_dto import UserDTO
from interfaces.i_auth_database import IAuthDatabase
from utils.logger import Logger


class AuthRepository(IAuthDatabase):
	def __init__(self, db_pool: pool, sql_manager: SQLManager, logging: Logger):
		self.db_pool = db_pool
		self.sql_manager = sql_manager
		self.logging = logging

	def get_user(self, username: str) -> Annotated[UserDTO, None]:
		with self.db_pool.getconn() as conn:
			with conn.cursor() as cur:
				self.logging.info(f'Getting user {username}')
				cur.execute(self.sql_manager.get_user, (username,))
				user = cur.fetchone()
				if user:
					return UserDTO(user[0], user[1], user[2])
				return None

	def add_user(self, user: UserDTO):
		with self.db_pool.getconn() as conn:
			with conn.cursor() as cur:
				self.logging.info(f'Adding user {user.username}')
				cur.execute(
					self.sql_manager.add_user,
					(user.username, user.password, user.data),
				)
				conn.commit()
				self.logging.info(f'User {user.username} added')

	def remove_user(self, username: str):
		with self.db_pool.getconn() as conn:
			with conn.cursor() as cur:
				self.logging.info(f'Removing user {username}')
				cur.execute(self.sql_manager.remove_user, (username,))
				conn.commit()
				self.logging.info(f'User {username} removed')
