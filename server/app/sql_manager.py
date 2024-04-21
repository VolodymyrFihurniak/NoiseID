from os import listdir
from typing import Annotated

from utils.logger import Logger


class SQLManagerError(Exception):
	pass


class SQLManager:
	_sqlmanager = None

	def __init__(self, logging: Logger) -> None:
		if not SQLManager._sqlmanager:
			SQLManager._sqlmanager = self
		self.queries = {}
		self.logging = logging
		self.logging.server.info('SQLManager instance created')

	def load_queries(self) -> None:
		sql_directory = 'sql'
		for file in listdir(sql_directory):
			if file.endswith('.sql'):
				with open(
					f'{sql_directory}/{file}', 'r', encoding='utf-8'
				) as f:
					self.queries[file.split('.')[0]] = f.read()
					self.logging.server.info(
						f'SQLManager query {file.split(".")[0]} loaded'
					)
		self.logging.server.info('SQLManager queries loaded')

	def get_query(self, query_name: str) -> Annotated[str, None]:
		query = self.queries.get(query_name)
		if not query:
			self.logging.server.error(
				f'SQLManager query {query_name} not found'
			)
			raise SQLManagerError(f'SQLManager query {query_name} not found')
		return query.strip()

	def set_up(self) -> None:
		self.load_queries()
		self.logging.server.info('SQLManager set up')
