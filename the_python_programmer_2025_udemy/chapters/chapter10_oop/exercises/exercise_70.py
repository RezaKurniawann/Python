# Exercise 70 - Shape and Square
# Write an abstract class called `Shape` with an abstractmethod `area`.
# Create two subclasses called `Square` and `Circle` that inherit from `Shape` and implement the `area` method.
# Modify the `Square` and `Circle` classes to accept whichever attributes are necessary to calculate the area.

# See `test_e70()` in `tests/test_ch10.py` for the expected behavior.

from abc import ABC, abstractmethod  # noqa: F401

PI = 3.14159


class Shape (ABC):
    @abstractmethod
    def area (self):
        pass


class Square(Shape):
    def __init__ (self, side: float):
        self.side = side

    def area (self):
        return round (self.side**2)


class Circle(Shape):
    def __init__ (self, radius: float):
        self.radius = radius

    def area (self):
        return round (PI * self.radius**2, 2)
