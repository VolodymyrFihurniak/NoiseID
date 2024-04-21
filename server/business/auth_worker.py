import numpy as np

from data.auth_repository import AuthRepository
from dtos.user_dto import UserDTO


class AuthWorker:
	def __init__(self, db: AuthRepository):
		self.db = db

	def calculate_hamming_distance(
		self, bitmap1: np.ndarray, bitmap2: np.ndarray
	) -> int:
		return np.sum(bitmap1 != bitmap2)

	def register(self, user: UserDTO):
		return self.db.add_user(user)

	def process_register(self, user):
		if self.db.get_user(user.username):
			return {'message': 'User already exists'}
		self.register(user)
		return {'message': 'User registered'}

	def login(self, user):
		return self.db.get_user(user.username)

	def process_login(self, user):
		db_user = self.login(user)
		if db_user:
			distance = self.calculate_hamming_distance(
				np.array(db_user.data, dtype=np.int16),
				np.array(user.data, dtype=np.int16),
			)
			if distance > 10:
				return {
					'message': f'User not recognized with distance {distance}'
				}
			return {'message': f'User recognized with distance {distance}'}
		return self.register(user)
