from functools import cached_property
from typing import List

from base.position import Position
from base.box import Boxable

from styling.endpoint import SeperableEndPointType
from styling.line import LineStyling
from styling.path import PathStyling

from .tech.positional import Positional
from .path import Path


class Line(Boxable, Positional[LineStyling], LineStyling):
    """This is the line as represented by the system. May consist of one or several paths"""
    outline: bool = False
    circle: bool = False
    _fill: bool = False
    _startEndpoint: SeperableEndPointType = None
    _endEndpoint: SeperableEndPointType = None

    def __init__(self, values: List[LineStyling], circle: bool = False, fill: bool = False, outline: bool = False, startEndpoint: bool = False, endEndpoint: bool = False, **kwargs):
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

        self.outline = outline
        self.circle = circle
        self.fill = fill
        self.startEndpoint = startEndpoint,
        self.endEndpoint = endEndpoint

        for ele in kwargs:
            setattr(self, ele, kwargs[ele])

    def __iadd__(self, value: LineStyling):
        self.values.append(value)

        if value.x<self.start.x:
            self.start.x = value.x
        if value.x>self.end.x:
            self.end.x = value.x
        if value.y<self.start.y:
            self.start.y = value.y
        if value.x>self.end.x:
            self.end.y = value.y

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

    @cached_property
    def outlinePath(self) -> Path:
        path: List[PathStyling] = []
        for position in self.values:
            path.append(position.topPath)
        if not self.circle:
            if self.endEndpoint:
                endPoint = position + self.endEndpoint
                path.append(PathStyling(endPoint.x, endPoint.y, position.colour, position.antialias, self.endEndpoint))
            for position in reversed(self.values):
                path.append(position.bottomPath)
            if self.startEndpoint:
                startPoint = position + self.startEndpoint
                path.append(PathStyling(startPoint.x, startPoint.y, position.colour, position.antialias, self.startEndpoint))
        return Path(path)

    @cached_property
    def fillPath(self) -> Path:
        if self.fill:
            return Path(self.values)