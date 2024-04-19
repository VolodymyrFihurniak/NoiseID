from app.sql_manager import SQLManager
from entities.config import Config
from utils.logger import Logger


class BaseController:
	def __init__(
		self, config: Config, db: None, sql_manager: SQLManager, logging: Logger
	) -> None:
		self.config = config
		self.db = db
		self.sql_manager = sql_manager
		self.logging = logging
