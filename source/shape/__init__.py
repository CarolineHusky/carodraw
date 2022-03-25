from dataclasses import dataclass
from base import Position
from path import Path

@dataclass
class Shape(Path):
	"""A shape is a :class:`path.Path` whose endpoint re-connects to its startpoint
	
..	image:: /../documentation/img/Shape.svg
	"""
	pass
