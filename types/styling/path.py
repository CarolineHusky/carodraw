from dataclasses import dataclass

from ..base.position import Position
from ..base.colour import Colour

from .endpoint import EndPointType

@dataclass
class PathStyling:
    """The styling of a path"""
    colour: Colour
    antialias: bool
    endpointType: EndPointType


@dataclass
class PathPointStyling(PathStyling, Position):
    """The styling at a given position, as used by paths"""
    pass