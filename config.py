import os
import logging
from dotenv import load_dotenv

if os.path.exists('config.env'):
    load_dotenv('config.env', override=True)


class Config:
    def __init__(self) -> None:
        self.SESSION: str = os.environ.get('SESSION', None)
        self.API_ID: str = os.environ.get('API_ID', None)
        self.API_HASH: str = os.environ.get('API_HASH', None)
        self.SUDO: list = [int(id) for id in os.environ.get(
            'SUDO', ' ').split() if id.isnumeric()]
        if not self.SESSION or not self.API_ID or not self.API_ID:
            print('Error: SESSION, API_ID and API_HASH is required.'
                  'Please check your config.env file.')
            quit(0)
        self.SPOTIFY: bool = False
        self.SPOTIFY_CLIENT_ID: str = os.environ.get('SPOTIFY_CLIENT_ID', None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            'SPOTIFY_CLIENT_SECRET', None)
        _log_level = os.environ.get('LOG_LEVEL', 'error').lower()
        if _log_level == 'error':
            self.LOG_LEVEL = logging.ERROR
        elif _log_level == 'info':
            self.LOG_LEVEL = logging.INFO
        elif _log_level == 'debug':
            self.LOG_LEVEL = logging.DEBUG
        else:
            self.LOG_LEVEL = logging.ERROR
        self.PREFIXES: list = os.environ.get('PREFIX', '/').split()
        self.DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'tr').lower()
        self.DEFAULT_STREAM_MODE: str = 'audio' if (os.environ.get(
            'DEFAULT_STREAM_MODE', 'audio').lower() == 'audio') else 'video'


config = Config()
