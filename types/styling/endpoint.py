from dataclasses import dataclass
from decimal import Decimal
import math

from ..base.position import Position

@dataclass
class EndPointType:
    """The styling of the endpoint, aka how round or smooth it is"""
    angle: Decimal
    rounding: Decimal


@dataclass
class SeperableEndPointType(EndPointType, Position):
    """The styling of the endpoint, including it's distance from the center"""
    seperation: Decimal

    @property
    def x(self):
        return self.seperation * math.cos(self.angle)

    @property
    def y(self):
        return self.seperation * math.sin(self.angle)