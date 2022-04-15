"""Module configuration"""
import sys
import logging

from os import environ
from pathlib import Path

from orangepi import oneplus

IS_TEST = any(map(lambda path: 'tests' in path, sys.path))  # If test paths are found, then go to test mode

DEBUG = bool(int(environ.get('DEBUG'))) or False
LOG_LEVEL = logging.getLevelName((environ.get('LOG_LEVEL') if not DEBUG else 'debug').upper())

DATA_PIN = int(environ.get('DATA_PIN'))
DATA_TIMEOUT = int(environ.get('DATA_TIMEOUT')) / 1000  # Converting timeout from milliseconds to seconds

SQLITE_ENGINE = f"sqlite:///{Path('/data', 'mammon.sqlite3')}"

logging.basicConfig(level=LOG_LEVEL,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

BOARD = oneplus.BOARD
