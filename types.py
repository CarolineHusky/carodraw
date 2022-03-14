from ctypes import Union
from dataclasses import dataclass, field
import dataclasses
from decimal import Decimal
from typing import Any, Dict, Generic, List, TypeVar


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

    def __add__(self, other):
        return Position(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Position(self.x-other.x, self.y-other.y)


@dataclass
class Colour:
    """
    A simple colour as used everywhere in the program. Don't use any system-specific colours for this purpose!
    
    Keyword arguments:
    red -- The value of the colour in its red spectrum, as an integer from 0 to 255
    green -- The value of the colour in its green spectrum, as an integer from 0 to 255
    blue -- The value of the colour in its blue spectrum, as an integer from 0 to 255
    alpha -- The transparancy of the colour, as an integer from 0 (transparant) to 255 (opaque)
    """
    red: int
    green: int
    blue: int
    alpha: int

    def __post_init__(self):
        self.red = int(max(0, min(255, self.red)))
        self.green = int(max(0, min(255, self.green)))
        self.blue = int(max(0, min(255, self.blue)))
        self.alpha = int(max(0, min(255, self.alpha)))

    def __eq__(self, other):
        return self.red==other.red and self.green==other.green and self.blue==other.blue and self.alpha==other.alpha


@dataclass
class Zone:
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

    def collideWithZone(self, zone) -> bool:
        """Checks if a zone collides with another zone"""
        if self.left > zone.right:
            return False
        if self.right > zone.left:
            return False
        if self.top > zone.bottom:
            return False
        if self.bottom > zone.top:
            return False
        return True


@dataclass
class Segment:
    """A line between two positions, and not outside them"""
    start: Position
    end: Position

    @property
    def zone(self) -> Zone:
        """Gets a zone bounding the segment"""
        return Zone(
            Position(self.start.x, self.start.y), 
            Position(self.end.x, self.end.y)
            )

    # 0 is startpoint, 1 is endpoint
    def split(self, percent: Decimal):
        """Splits a segment along a splitpoint"""
        midpoint = Position(self.start.x * (1-percent) + self.end.x * percent, self.start.y * (1-percent) + self.end.y * percent)
        return [Segment(self.start, midpoint), Segment(midpoint, self.end)]

    def inZone(self, zone: Zone) -> bool:
        """Checks if a segment's bounding box collides with another bounding box. Does *not* check if it actually touches it"""
        return self.zone.collideWithZone(zone)

        

@dataclass
class Styling:
    """
    A styling definition

    Keyword arguments:
    thickness -- The width of the pen
    colour -- The colour of the pen
    """
    thickness: Decimal
    colour: Colour
