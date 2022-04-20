"""Module describing work with money protocols"""
import OPi.GPIO

from mammon_gpio.gpio import GPIO


class MoneyGPIO(GPIO):
    """Class for working with protocols for transferring data on receipt of money"""

    # pylint: disable=W1113
    def __init__(self, data_pin: int, count_per_pulse: float = 1.0, timeout: float = 1.0, *args, **kwargs):
        """
        Class for working with protocols for transferring data on receipt of money
        Args:
            data_pin: int: Pin to which Pulse signals are applied
            count_per_pulse: float: Significance of one pulse: ex: 1 pulse - 5$, therefore 6 pulses - 30$
            timeout: float: Timeout for receiving pulses in seconds
        """
        super().__init__(*args, **kwargs)
        self.data_pin = data_pin
        self.count_per_pulse = count_per_pulse
        self.timeout = timeout
        self.currency = 0

    def init_pins(self):
        """Pin direction initialization"""
        OPi.GPIO.setup(self.data_pin, OPi.GPIO.IN)

    @property
    def money(self) -> float:
        """Get the total amount of money received"""
        return self.currency * self.count_per_pulse

    def clear_money(self):
        """Clear counted money"""
        self.currency = 0
