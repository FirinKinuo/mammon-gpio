import time

from datetime import datetime
from logging import getLogger

import OPi.GPIO

from mammon_gpio.settings import config
from mammon_gpio.db.replenishment import ReplenishmentHistory
from mammon_gpio.gpio.pulse import PulseMoney, MoneyGPIO

log = getLogger("main")


def start_loop(money_gpio: MoneyGPIO):
    while True:
        if money_gpio.money and pulse.is_timeout:
            log.info(f"Money received: {money_gpio.money}")

            ReplenishmentHistory.set(datetime=datetime.now(), currency=money_gpio.money)

            money_gpio.clear_money()

        time.sleep(1)


if __name__ == "__main__":
    print(f"Start Mammon GPIO at PIN: {config.DATA_PIN}")

    pulse = PulseMoney(
        data_pin=config.DATA_PIN,
        board=config.BOARD,
        timeout=config.DATA_TIMEOUT
    )

    pulse.init_gpio()

    try:
        start_loop(money_gpio=pulse)
    finally:
        OPi.GPIO.cleanup()
