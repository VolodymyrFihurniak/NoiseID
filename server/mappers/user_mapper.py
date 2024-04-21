from dtos.user_dto import UserDTO
from entities.user import User
from mappers import BaseMapper


class UserMapper(BaseMapper):
	def to_dto(self, user, data) -> UserDTO:
		return UserDTO(user.username, user.password, data)

	def to_entity(self, data: UserDTO) -> User:
		return User(data.dataname, data.password, data.data)
