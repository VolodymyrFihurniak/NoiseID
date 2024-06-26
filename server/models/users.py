from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from models.base import Base


class UserDB(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    authentification = mapped_column(
        Integer, ForeignKey('authentifications.id'))
