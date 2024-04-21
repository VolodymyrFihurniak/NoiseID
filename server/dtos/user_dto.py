class UserDTO:
	def __init__(self, username: str, password: str, data: list[int]) -> None:
		self.username = username
		self.password = password
		self.data = data
