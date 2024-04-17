class UserDTO:
    def __init__(
            self,
            username: str,
            password: str,
            data: list
    ):
        self.username = username
        self.password = password
        self.data = data
