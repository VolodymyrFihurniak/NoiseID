from sqlalchemy import Integer, String, ARRAY
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel
from models.base import Base


class AuthentificationDB(Base):
	__tablename__ = 'authentifications'
	__table_args__ = {'extend_existing': True}

	id = mapped_column(Integer, primary_key=True)
	username = mapped_column(String)
	password = mapped_column(String)
	data = mapped_column(ARRAY(Integer))


class Authentification(BaseModel):
	username: str
	password: str
