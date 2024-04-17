from business.auth_worker import AuthWorker
from core.microphone_recorder import Microphone
from data.auth_service import AuthService
from entities.config import Config
from utils.logger import Logger


class AuthController:
    def __init__(self, logging: Logger, config: Config):
        self.logging = logging
        self.config = config

    def build_auth_worker(self):
        return AuthWorker(
            self.logging,
            AuthService(self.logging, self.config)
        )

    def login(self, username: str, password: str, microphone: Microphone):
        self.logging.app.debug(f"Username: {username}, Password: "
                               f"{password}, Index device: {microphone.index}"
                               f", Name device: {microphone.name}")
        worker = self.build_auth_worker()
        return worker.login(username, password, microphone)
