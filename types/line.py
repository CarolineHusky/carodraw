from functools import cached_property
from typing import List

from base.position import Position
from base.box import Boxable

from styling.endpoint import SeperableEndPointType
from styling.line import LineStyling, LinePointStyling
from styling.path import PathPointStyling

from .tech.positional import Positional
from .path import Path


class Line(Boxable, Positional[LineStyling], LineStyling):
    """This is the line as represented by the system. May consist of one or several paths"""

    def __init__(self, values: List[LinePointStyling], circle: bool = False, fill: bool = False, outline: bool = False, startEndpoint: bool = False, endEndpoint: bool = False, **kwargs):
        self.values = values
        self.start = Position(values[0].x, values[0].y)
        self.end = Position(values[0].x, values[0].y)
        for value in self.values:
            self.patchBox(value)

        self.outline = outline
        self.circle = circle
        self.fill = fill
        self.startEndpoint = startEndpoint,
        self.endEndpoint = endEndpoint

        for ele in kwargs:
            setattr(self, ele, kwargs[ele])

    def __iadd__(self, value: LinePointStyling):
        self.values.append(value)

        self.patchBox(value)

        del self.outlinePath
        del self.fillPath


    @property
    def fill(self) -> bool:
        return self.circle and self._fill

    @property.setter
    def fill(self, value: bool):
        if value != self._fill:
            self._fill = value
            del self.fillPath
        self._fill = value
        self.circle = self.circle or value

    @property
    def startEndpoint(self) -> SeperableEndPointType:
        return (not self.circle) and self._startEndpoint

    @property.setter
    def startEndpoint(self, value: SeperableEndPointType):
        self._startEndpoint = value
        if value:
            self.circle = False
            self.fill = False
            del self.outlinePath

    @property
    def endEndpoint(self) -> SeperableEndPointType:
        return (not self.circle) and self._endEndpoint

    @property.setter
    def endEndpoint(self, value: SeperableEndPointType):
        self._endEndpoint = value
        if value:
            self.circle = False
            self.fill = False
            del self.outlinePath

    @property
    def topPath(self) -> Path:
        path: List[PathPointStyling] = []
        for position in self.values:
            self.patchBox(position.topPath)
            path.append(position.topPath)
        return Path(path)

    @property
    def bottomPath(self) -> Path:
        path: List[PathPointStyling] = []
        for position in reversed(self.values):
            self.patchBox(position.bottomPath)
            path.append(position.bottomPath)
        return Path(path)

    @cached_property
    def outlinePath(self) -> Path:
        path = self.topPath
        if not self.circle:
            if self.endEndpoint:
                endPoint = self.values[-1] + self.endEndpoint
                self.patchBox(endPoint)
                path += + Path([PathPointStyling(endPoint.x, endPoint.y, self.values[-1].colour, self.values[-1].antialias, self.endEndpoint)])
            path += self.bottomPath
            if self.startEndpoint:
                startPoint = self.values[0] + self.startEndpoint
                self.patchBox(startPoint)
                path += Path([PathPointStyling(startPoint.x, startPoint.y, self.values[-1].colour, self.values[-1].antialias, self.startEndpoint)])
        return path

    @cached_property
    def fillPath(self) -> Path:
        if self.fill:
            return self.bottomPath