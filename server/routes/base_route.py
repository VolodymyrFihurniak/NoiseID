from abc import ABC, abstractmethod
from fastapi import APIRouter


class BaseRoute(ABC):
    def __init__(self, router: APIRouter, name: str, config, db) -> None:
        self.router = router
        self.name = name
        self.config = config
        self.db = db

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def configure_routes(self) -> APIRouter:
        pass
