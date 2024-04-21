from data.auth_repository import AuthRepository
from dtos.user_dto import UserDTO


class AuthWorker:
	def __init__(self, db: AuthRepository):
		self.db = db

	def register(self, user: UserDTO):
		if self.db.get_user(user.username):
			return None
		return self.db.add_user(user)

	def login(self, user):
		return self.db.get_user(user.username)

	def process_login(self, user):
		user = self.login(user)
		if user:
			return user
		return self.register(user)
