"""Module for working with GPIO"""
import OPi.GPIO


class GPIO:
    """Base class for working with GPIO"""

    def __init__(self, board: dict):
        """
        Base class for working with GPIO
        Args:
            board: dict: GPIO pinout dictionary
                         Ready-made dictionaries can be found in nanopi, orangepi, rockpi, etc... packages.
        """
        self.board = board

    def init_board(self):
        """Initialize board type with GPIO pinout"""
        OPi.GPIO.setmode(self.board)

    # pylint: disable=W2301,R0201
    def init_gpio(self):
        """Method template for initializing GPIO"""
        ...
