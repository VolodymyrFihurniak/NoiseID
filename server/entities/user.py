class User:
	def __init__(self, username: str, password: str, data: list[int]):
		self.username = username
		self.password = password
		self.data = data

	def __str__(self):
		return f'User {self.username}'
