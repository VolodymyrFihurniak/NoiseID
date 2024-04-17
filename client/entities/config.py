from __future__ import annotations
from collections import OrderedDict


class AppModelConfig:
    server_domain: str
    server_port: int

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.server_domain = env.get(
            'app_server_domain') or config['app']['server_domain']
        self.server_port = env.get(
            'app_server_port') or config['app']['server_port']


class MicrophoneModelConfig:
    rate: int
    frames_per_buffer: int
    duration: int
    max_signals: int

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.rate = env.get(
            'microphone_rate') or config['microphone']['rate']
        self.frames_per_buffer = env.get(
            'microphone_frames_per_buffer') or config['microphone']['frames_per_buffer']
        self.duration = env.get(
            'microphone_duration') or config['microphone']['duration']
        self.max_signals = env.get(
            'microphone_max_signals') or config['microphone']['max_signals']


class StylesModelConfig:
    root_frame: dict
    main_frame: dict

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.root_frame = env.get(
            'styles_root_frame') or config['styles']['root_frame']
        self.main_frame = env.get(
            'styles_main_frame') or config['styles']['main_frame']


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
    microphone: MicrophoneModelConfig = None
    styles: StylesModelConfig = None
    logging: LoggingModelConfig = None

    def __init__(self, env: OrderedDict, config: dict) -> None:
        self.app = AppModelConfig(env, config)
        self.microphone = MicrophoneModelConfig(env, config)
        self.styles = StylesModelConfig(env, config)
        self.logging = LoggingModelConfig(env, config)
