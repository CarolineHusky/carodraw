
from dataclasses import dataclass
from decimal import Decimal

from .position import Position

class Boxable:
    """
    An element that has a boundary box. Defines start and end
    """
    @property
    def top(self) -> Decimal:
        """The top side of the zone"""
        return self.start.y

    @property
    def left(self) -> Decimal:
        """The left side of the zone"""
        return self.start.x

    @property
    def bottom(self) -> Decimal:
        """The bottom side of the zone"""
        return self.end.y

    @property
    def right(self) -> Decimal:
        """The right side of the zone"""
        return self.end.x

    @property
    def topLeft(self) -> Decimal:
        """The top-left corner of the zone"""
        return self.start

    @property
    def topRight(self) -> Decimal:
        """The top-right corner of the zone"""
        return Position(self.right, self.top)

    @property
    def bottomLeft(self) -> Decimal:
        """The bottom-left corner of the zone"""
        return Position(self.left, self.bottom)

    @property
    def bottomRight(self) -> Decimal:
        """The bottom-right corner of the zone"""
        return self.end

    @property
    def width(self) -> Decimal:
        """The width of the zone. Aka the distance on the horizontal axis between left and right"""
        return self.end.x - self.start.x

    @property
    def height(self) -> Decimal:
        """The height of the zone. Aka the distance on the vertical axis between top and bottom"""
        return self.end.y - self.start.y

    def collideWithBoundaryBox(self, zone) -> bool:
        """Checks if a boundary box collides with another boundary box"""
        if self.left > zone.right:
            return False
        if self.right > zone.left:
            return False
        if self.top > zone.bottom:
            return False
        if self.bottom > zone.top:
            return False
        return True

    def patchBox(self, value: Position):
        if value.x<self.start.x:
            self.start.x = value.x
        if value.x>self.end.x:
            self.end.x = value.x
        if value.y<self.start.y:
            self.start.y = value.y
        if value.x>self.end.x:
            self.end.y = value.y



@dataclass
class BoundaryBox(Boxable):
    """
    A rectangle with axis aligned to the horizontal and vertical axis. Only need two entities to be defined. Start always contains the top-left corner and End always contain the bottom-right corner, even if initialised otherwise
    
    Keyword arguments:
    start -- the top-left corner of the zone
    end -- the bottom-right corner of the zone
    """
    start: Position
    end: Position

    def __post_init__(self):
        """Correctly set the top-left and bottom-right corners"""
        if self.start.x>self.end.x:
            self.start.x, self.end.x = self.end.x, self.start.x
        if self.start.y>self.end.y:
            self.start.y, self.end.y = self.end.y, self.start.y