import json

from core.microphone_recorder import Microphone
from data.auth_service import AuthService
from dtos.user_dto import UserDTO
from utils.logger import Logger


class AuthWorker:
    def __init__(self, logging: Logger, auth_service: AuthService):
        self.logging = logging
        self.auth_service = auth_service

    def login(self, username: str, password: str, microphone: Microphone) -> json.JSONEncoder:
        user = UserDTO(username, password, [])
        result = self.auth_service.login(user, microphone)
        return {'message': result}
