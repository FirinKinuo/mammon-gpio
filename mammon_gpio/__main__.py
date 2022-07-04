import time

from datetime import datetime
from logging import getLogger


from mammon_gpio.settings import config
from mammon_gpio.db.replenishment import ReplenishmentHistory
from mammon_gpio.gpio.pulse import PulseMoney, MoneyGPIO
import OPi.GPIO

log = getLogger("main")


def start_loop(money_gpio: MoneyGPIO):
    while True:
        if money_gpio.money and pulse.is_timeout:
            log.info(f"Money received: {money_gpio.money}")
            replenishment_datetime = datetime.now()

            ReplenishmentHistory.set(datetime=replenishment_datetime, currency=money_gpio.money)

            money_gpio.clear_money()

        time.sleep(0.015)


if __name__ == "__main__":
    print(f"Start Mammon GPIO at PIN: {config.DATA_PIN}")

    pulse = PulseMoney(
        data_pin=config.DATA_PIN,
        board=config.BOARD,
        timeout=config.DATA_TIMEOUT,
        count_per_pulse=config.COUNT_PER_PULSE
    )

    pulse.init_gpio()

    try:
        start_loop(money_gpio=pulse)
    finally:
        OPi.GPIO.cleanup()
