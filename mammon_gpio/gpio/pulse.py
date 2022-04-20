"""Module describing how to work with the Pulse protocol"""
from datetime import datetime

import OPi.GPIO

from mammon_gpio.gpio.money import MoneyGPIO


class PulseMoney(MoneyGPIO):
    """Class for working with the Pulse protocol"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.first_pulse_timestamp = datetime.now().timestamp()
        self.last_pulse_timestamp = self.first_pulse_timestamp

    def init_gpio(self):
        """GPIO initialization"""
        self.init_board()
        self.init_pins()
        self.bind_pulse_pin_counter()

    def bind_pulse_pin_counter(self):
        """Bind the counting function to a logic pin interrupt"""
        OPi.GPIO.add_event_detect(
            channel=self.data_pin,
            trigger=OPi.GPIO.FALLING,
            callback=self.count_pulse,
        )

    def _increase_currency(self):
        self.currency += 1

    def check_bounce_time(self, bounce_time: float = 0.015) -> bool:
        """
        Delay check to avoid contact bounce
        Args:
            bounce_time: float: Delay time in seconds

        Returns:
            bool - Is the time for anti-bounce over
        """
        return datetime.now().timestamp() - self.last_pulse_timestamp >= bounce_time

    def count_pulse(self, *args, **kwargs):  # pylint: disable=W0613
        """Counting the number of pulses"""
        if self.check_bounce_time(bounce_time=0.015):
            self._increase_currency()
            self.last_pulse_timestamp = datetime.now().timestamp()

        if self.currency == 1:
            self.first_pulse_timestamp = self.last_pulse_timestamp
