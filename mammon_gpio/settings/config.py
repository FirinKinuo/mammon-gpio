"""Module configuration"""
import logging

from os import environ

from mammon_gpio.settings.mappings import mappers


def _check_board(manufacturer: str, model: str) -> bool:
    return manufacturer in mappers.keys() and model in mappers[manufacturer].keys()


DEBUG = bool(int(environ.get('DEBUG'))) or False
LOG_LEVEL = logging.getLevelName((environ.get('LOG_LEVEL') if not DEBUG else 'debug').upper())

DATA_PIN = int(environ.get('DATA_PIN'))
DATA_TIMEOUT = int(environ.get('DATA_TIMEOUT')) / 1000  # Converting timeout from milliseconds to seconds
COUNT_PER_PULSE = float(environ.get('COUNT_PER_PULSE') or 1.0)
MINIMAL_MONEY = int(environ.get('MINIMAL_MONEY') or 1)
SQLITE_ENGINE = f"sqlite:////data/mammon.sqlite3"

BOARD_MANUFACTURER = environ.get('BOARD_MANUFACTURER').lower()
BOARD_MODEL = environ.get('BOARD_MODEL').lower()

logging.basicConfig(level=LOG_LEVEL,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

if not _check_board(manufacturer=BOARD_MANUFACTURER, model=BOARD_MODEL):
    logging.critical(f"Manufacturer {BOARD_MANUFACTURER} or board model {BOARD_MODEL} not supported!")

BOARD = mappers[BOARD_MANUFACTURER][BOARD_MODEL]
