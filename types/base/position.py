from dataclasses import dataclass
from decimal import Decimal
from __future__ import annotations

@dataclass
class Position:
    """
    A position in space. We intentionally don't define its limits
    
    Keyword arguments:
    x -- The position in its horizontal axis
    y -- The position in its vertical axis
    """
    x: Decimal
    y: Decimal

    def __add__(self, other: Position):
        return Position(self.x+other.x, self.y+other.y)

    def __sub__(self, other: Position):
        return Position(self.x-other.x, self.y-other.y)

    def __mul__(self, other: Decimal):
        return Position(self.x * other, self.y * other)