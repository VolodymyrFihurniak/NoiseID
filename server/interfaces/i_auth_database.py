from abc import ABC, abstractmethod
from typing import Annotated

from dtos.user_dto import UserDTO


class IAuthDatabase(ABC):
	@abstractmethod
	def get_user(self, username: str) -> Annotated[UserDTO, None]:
		pass

	@abstractmethod
	def add_user(self, user: UserDTO) -> None:
		pass

	@abstractmethod
	def remove_user(self, username: str) -> None:
		pass
