import pygame

from types import AmbiguousPositionalException, ColourSet, Position, StyledSegment, Zone

from .canvas import Canvas as RawCanvas, RedrawDirty

pygame.init()

class Canvas(RawCanvas):
    error: Position = None
    def __init__(self):
        width = 1200
        height = 700
        super().init(Zone(Position(-width/2, -height/2), Position(width/2, height/2)))
        
    def resize(self, zone: Zone):
        self.surface = pygame.Surface((self.zone.width, self.zone.height), pygame.SRCALPHA)
        super().resize(zone)

    def refresh(self) -> None:
        self.surface.fill(( 0, 0, 0, 0))
        super().refresh()

    def moveCanvas(self, diff: Position) -> None:
        self.surface.scroll(int(diff.x), int(diff.y))
        self.error=Position(diff.x-int(diff.x), diff.y-int(diff.y))
        super().moveCanvas(diff)

    def redraw_dirty(self, event: RedrawDirty) -> None:
        self.surface.fill((0,0,0,0), pygame.Rect(event.start.x, event.start.y, event.width, event.height))
        for segment in event.segments:
            self.draw_segment(segment)
        return super().redraw_dirty(event)

    def draw_segment(self, segment: StyledSegment) -> None:
        try:
            colour = pygame.Color(segment.colour.red, segment.colour.green, segment.colour.blue, segment.colour.alpha)
            pygame.draw.line(self.surface, colour, (segment.start.x, segment.start.y), (segment.end.x, segment.end.y), width=1)
        except AmbiguousPositionalException:
            raise NotImplementedError