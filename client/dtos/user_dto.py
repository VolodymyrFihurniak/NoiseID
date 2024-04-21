class UserDTO:
    def __init__(
            self,
            username: str,
            password: str,
            data: bytes
    ):
        self.username = username
        self.password = password
        self.data = data

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
        }
