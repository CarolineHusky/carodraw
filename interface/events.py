
from dataclasses import dataclass
from decimal import Decimal

from carotools.events import Event, on

from .canvas import Canvas
from ..types import Position, Zone, StyledSegment
from ..types import Segment as RawSegment
from ..events import RevertableEvent


@dataclass
class MarkAsDirty(Event, Zone):
    canvas: Canvas

@on(MarkAsDirty)
def markAsDirty(event: MarkAsDirty):
    event.canvas.dirty_zones.append(event)


@dataclass
class RedrawDirty(Event, Zone):
    canvas: Canvas

@on(RedrawDirty)
def redrawDirty(event: RedrawDirty):
    event.canvas.redraw_dirty(event)

@on(RedrawDirty)
def redrawDirty_gatherSegments(event: RedrawDirty):
    event.segments = event.canvas.redrawDirty_gatherSegments(event)


@dataclass
class Redraw(Event):
    canvas: Canvas
    centerPoint: Position
    scale: Decimal


@dataclass
class Refresh(Event):
    canvas: Canvas

@on(Refresh)
def refresh(event: Refresh):
    event.canvas.refresh()


@dataclass
class MoveCanvas(Event, Position):
    canvas: Canvas

@on(MoveCanvas)
def moveCanvas(event: MoveCanvas):
    event.canvas.moveCanvas(event-event.canvas.centerPoint)


@dataclass
class Resize(Event, Zone):
    canvas: Canvas

@on(Resize)
def resize(event: Resize):
    event.canvas.resize(event)


@dataclass
class Segment(RevertableEvent, RawSegment):
    canvas: Canvas

def remove_segment(event: Segment):
    event.canvas.segmentData.remove(event.styled_segment)

@on(Segment, revert=remove_segment)
def add_segment(event: Segment):
    event.styled_segment = StyledSegment(event.start, event.end, event.colour)
    event.canvas.addSegment(event.styled_segment)
    MarkAsDirty(event.zone.start, event.zone.end, event.canvas)
    