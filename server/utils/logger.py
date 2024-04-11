import datetime
import logging
import logging.config


from pathlib import Path

from entities.config import Config


class Logger:
    def __init__(self, config: Config) -> None:
        logging_dir = Path(config.logging.log_dir)
        if not logging_dir.exists():
            logging_dir.mkdir(parents=True)
        logging_config_file = Path(config.logging.config_path).resolve()
        logging.config.fileConfig(logging_config_file,
                                  defaults={
                                      'asctime': datetime.datetime.now().strftime('%Y-%m-%d')},
                                  encoding='utf-8')
        self.server = logging.getLogger('server')
        self.business = logging.getLogger('business')
        self.data = logging.getLogger('data')
