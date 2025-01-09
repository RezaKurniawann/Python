# Exercise 84 - Log This
# Given this "RateInterestCalculator" class with two methods,
# we need to replace the print() messages with log statements instead with
# the appropriate Log Level.

# Can you fix this?

import logging  # noqa: F401

class RateInterestCalculator:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
 
    def calculate_rate(self) -> None:
        self.logger.info("Calculating rate...")
        self.logger.error("An error occurred while calculating the rate")
 
    def calculate_interest(self) -> None:
        self.logger.info("Calculating interest...")
