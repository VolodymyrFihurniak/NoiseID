from abc import ABC, abstractmethod


class BaseMapper(ABC):
	@abstractmethod
	def to_dto(self, user, data):
		pass

	@abstractmethod
	def to_entity(self, data):
		pass
