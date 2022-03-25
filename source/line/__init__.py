from path import Path
from path.endpoint import StyledEndPoint
from dataclasses import dataclass


@dataclass
class Line(Path):
	"""
	This is a `Line` which ain't connected to anything, connecting its `startPoint` to its `endPoint`.
    
..	image:: /../documentation/img/Isolate.svg
	"""
	
	startPoint: StyledEndPoint
	"""The start point of the `Isolate`. Can be positioned in the canvas or relative to the area of another shape. Contains endpoint styling."""
	
	endPoint: StyledEndPoint
	"""The end point of the `Isolate`. Can be positioned in the canvas or relative to the area of another shape. Contains endpoint styling."""
