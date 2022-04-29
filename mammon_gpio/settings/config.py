"""Module configuration"""
import logging

from os import environ

from mammon_gpio.settings import mappings

DEBUG = bool(int(environ.get('DEBUG'))) or False
LOG_LEVEL = logging.getLevelName((environ.get('LOG_LEVEL') if not DEBUG else 'debug').upper())

DATA_PIN = int(environ.get('DATA_PIN'))
DATA_TIMEOUT = int(environ.get('DATA_TIMEOUT')) / 1000  # Converting timeout from milliseconds to seconds
COUNT_PER_PULSE = float(environ.get('COUNT_PER_PULSE') or 1.0)
SQLITE_ENGINE = f"sqlite:////data/mammon.sqlite3"

logging.basicConfig(level=LOG_LEVEL,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

# TODO: Make mapping configuration via env
BOARD = mappings.raspberry

