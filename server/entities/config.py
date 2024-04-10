from __future__ import annotations
from collections import OrderedDict
from pydantic import BaseModel, ValidationError


class AppYAMLConfig(BaseModel):
    host: str
    port: int
    use_https: bool


class DBYAMLConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str


class LoggingYAMLConfig(BaseModel):
    config_path: str
    log_dir: str


class AppDotEnvConfig(BaseModel):
    app_host: str
    app_port: int
    app_use_https: bool


class DBDotEnvConfig(BaseModel):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_database: str


class LoggingDotEnvConfig(BaseModel):
    logging_config_path: str
    logging_log_dir: str


class Config:
    app: AppYAMLConfig | AppDotEnvConfig = None
    db: DBYAMLConfig | DBDotEnvConfig = None
    logging: LoggingYAMLConfig | LoggingDotEnvConfig = None

    def __init__(self, config: dict, env:  OrderedDict) -> None:
        try:
            self.app = AppDotEnvConfig(**env)
        except ValidationError:
            self.app = AppYAMLConfig(**config['app'])
        try:
            self.db = DBDotEnvConfig(**env)
        except ValidationError:
            self.db = DBYAMLConfig(**config['db'])
        try:
            self.logging = LoggingDotEnvConfig(**env)
        except ValidationError:
            self.logging = LoggingYAMLConfig(**config['logging'])
