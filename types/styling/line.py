from dataclasses import dataclass

from ..base.colour import Colour

from .path import PathStyling
from .endpoint import SeperableEndPointType


@dataclass
class LineStyling(PathStyling):
    """The styling at a given position, as used by (drawed) lines"""
    fillColour: Colour
    endpointType: SeperableEndPointType
    invertTopBottom: bool = False

    @property
    def topPath(self):
        if self.invertTopBottom:
            return PathStyling(self.x + self.endpointType.x, self.y + self.endpointType.y, self.colour, self.antialias, self.endpointType)
        return PathStyling(self.x - self.endpointType.x, self.y - self.endpointType.y, self.colour, self.antialias, self.endpointType)

    @property
    def bottomPath(self):
        if self.invertTopBottom:
            return PathStyling(self.x - self.endpointType.x, self.y - self.endpointType.y, self.colour, self.antialias, self.endpointType)
        return PathStyling(self.x + self.endpointType.x, self.y + self.endpointType.y, self.colour, self.antialias, self.endpointType)