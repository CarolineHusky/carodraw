from dataclasses import dataclass
from decimal import Decimal
from typing import Generator, List
from carotools.events import Event, on

from .events import MarkAsDirty, MoveCanvas, RedrawDirty, Refresh, Resize
from ..events import RevertableEvent

from ..types import Position, StyledSegment, Zone
from ..types import Segment as RawSegment


class Canvas:
    def __init__(self, zone) -> None:
        self.centerPoint = Position(0,0)
        self.scale: Decimal = 1
        Resize(zone.start, zone.end, self)

        self.segmentData: List[StyledSegment] = []

    def resize(self, zone: Zone) -> None:
        self.zone = zone
        Refresh(self)

    def refresh(self) -> None:
        self.dirty_zones: List[Zone] = [self.zone]

    def moveCanvas(self, diff: Position) -> None:
        if diff.x < 0:
            MarkAsDirty(self, 
                Zone(
                    self.zone.topLeft, 
                    Position(self.zone.left-diff.x, self.zone.bottom)))
                    
        if diff.x > 0:
            MarkAsDirty(self, 
                Zone(
                    Position(self.zone.right-diff.x, self.zone.top), 
                    self.zone.bottomRight))

        if diff.y < 0:
            MarkAsDirty(self, 
                Zone(
                    self.zone.topLeft, 
                    Position(self.zone.right, self.zone.bottom-diff.y)))

        if diff.y > 0:
            MarkAsDirty(self, 
                Zone(
                    Position(self.zone.left, self.zone.bottom-diff.y), 
                    self.zone.bottomRight))

        self.centerPoint = self.centerPoint + diff

    def redraw(self, centerPoint, scale) -> None:
        if(scale != self.scale):
            Refresh(self)
        elif(centerPoint != self.centerPoint):
            MoveCanvas(centerPoint.x, centerPoint.y, self)

    def redraw_dirty(self, event: RedrawDirty) -> None:
        pass

    def draw_segment(self, segment: StyledSegment) -> None:
        pass

    def addSegment(self, segment: StyledSegment) -> None:
        self.segmentData.append(segment)

    def removeSegment(self, segment: StyledSegment) -> None:
        self.segmentData.remove(segment)

    def redrawDirty_gatherSegments(self, event: RedrawDirty) -> Generator[StyledSegment]:
        for segment in self.segmentData:
            if segment.inZone(event):
                yield segment

