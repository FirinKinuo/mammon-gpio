import time

from datetime import datetime
from logging import getLogger

import OPi.GPIO

from mammon_gpio.settings import config
from mammon_gpio.db.replenishment import ReplenishmentHistory
from mammon_gpio.gpio.pulse import PulseMoney, MoneyGPIO

log = getLogger("main")


def clear_if_replenishment_repeated(datetime_: datetime) -> bool:
    replenishment = ReplenishmentHistory.get_pool_by_datetime(
        start_datetime=datetime_.replace(microsecond=0),
        end_datetime=datetime.now())
    if replenishment:
        log.info("Duplicate replenishment detected")
        [r.delete() for r in replenishment]
        return True

    return False


def start_loop(money_gpio: MoneyGPIO):
    while True:
        if money_gpio.money and pulse.is_timeout:
            log.info(f"Money received: {money_gpio.money}")

            replenishment_datetime = datetime.now()

            # Signal surge protection when the wash post is turned on
            if clear_if_replenishment_repeated(datetime_=replenishment_datetime):
                continue

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
