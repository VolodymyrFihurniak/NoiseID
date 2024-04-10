from __future__ import annotations
from collections import OrderedDict


class AppModelConfig:
    host: str
    port: int
    use_https: bool
    ssl_key_path: str
    ssl_cert_path: str

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.host = env.get('app_host') or config['app']['host']
        self.port = int(env.get('app_port')) or int(config['app']['port'])
        self.use_https = bool(env.get('app_use_https')) or bool(
            config['app']['use_https'])
        self.ssl_key_path = env.get(
            'app_ssl_key_path') or config['app']['ssl_key_path']
        self.ssl_cert_path = env.get(
            'app_ssl_cert_path') or config['app']['ssl_cert_path']


class DBModelConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.host = env.get('db_host') or config['db']['host']
        self.port = env.get('db_port') or config['db']['port']
        self.user = env.get('db_user') or config['db']['user']
        self.password = env.get('db_password') or config['db']['password']
        self.database = env.get('db_database') or config['db']['database']


class LoggingModelConfig:
    config_path: str
    log_dir: str

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.config_path = env.get(
            'logging_config_path') or config['logging']['config_path']
        self.log_dir = env.get(
            'logging_log_dir') or config['logging']['log_dir']


class Config:
    app: AppModelConfig = None
    db: DBModelConfig = None
    logging: LoggingModelConfig = None

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.app = AppModelConfig(env, config)
        self.db = DBModelConfig(env, config)
        self.logging = LoggingModelConfig(env, config)
