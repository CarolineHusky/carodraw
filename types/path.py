from typing import List

from .base.box import Boxable
from .base.position import Position

from .tech.positional import Positional

from .styling.path import PathStyling, PathPointStyling


class Path(Boxable, Positional[PathStyling], PathStyling):
    """This is used internally to draw lines."""

    def __init__(self, values: List[PathPointStyling], **kwargs):
        """Correctly set the top-left and bottom-right corners"""
        self.values = values
        left = None
        top = None
        right = None
        bottom = None
        for value in self.values:
            if left == None or value.x<left:
                left = value.x
            if right == None or value.x>right:
                right = value.x
            if top == None or value.y<top:
                top = value.y
            if bottom == None or value.y>bottom:
                bottom = value.y
        self.start = Position(left, top)
        self.end = Position(bottom, right)
        for ele in kwargs:
            setattr(self, ele, kwargs[ele])

    def __add__(self, other: Positional[PathPointStyling]):
        return Path(self.values + other.values)

    def __iadd__(self, other: Positional[PathPointStyling]):
        for value in other.values:
            self.values.append(value)
            self.patchBox(value)