import time

from datetime import datetime

import OPi.GPIO

from mammon_gpio.settings import config
from mammon_gpio.gpio.pulse import PulseMoney


# TODO: Normal start, this is still a temporary solution for displaying health
if __name__ == "__main__":
    print(f"Start Mammon GPIO at PIN: {config.DATA_PIN}")
    pulse = PulseMoney(
        data_pin=config.DATA_PIN,
        board=config.BOARD,
        timeout=config.DATA_TIMEOUT
    )

    pulse.init_gpio()

    try:
        while True:
            time.sleep(0.1)

            if pulse.currency and (datetime.now().timestamp() - pulse.first_pulse_timestamp) >= pulse.timeout:
                print(pulse.currency)

                pulse.currency = 0
    finally:
        OPi.GPIO.cleanup()
