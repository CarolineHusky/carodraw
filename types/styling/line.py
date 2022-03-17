from dataclasses import dataclass

from ..base.colour import Colour

from .path import PathStyling, PathPointStyling
from .endpoint import SeperableEndPointType


@dataclass
class LineStyling(PathStyling):
    """The styling of a line"""
    fillColour: Colour
    endpointType: SeperableEndPointType
    invertTopBottom: bool = False


@dataclass
class LinePointStyling(LineStyling, PathPointStyling):
    """The styling at a given position, as used by (drawed) lines"""

    @property
    def topPath(self) -> PathPointStyling:
        if self.invertTopBottom:
            return PathPointStyling(self.x + self.endpointType.x, self.y + self.endpointType.y, self.colour, self.antialias, self.endpointType)
        return PathPointStyling(self.x - self.endpointType.x, self.y - self.endpointType.y, self.colour, self.antialias, self.endpointType)

    @property
    def bottomPath(self) -> PathPointStyling:
        if self.invertTopBottom:
            return PathPointStyling(self.x - self.endpointType.x, self.y - self.endpointType.y, self.colour, self.antialias, self.endpointType)
        return PathPointStyling(self.x + self.endpointType.x, self.y + self.endpointType.y, self.colour, self.antialias, self.endpointType)