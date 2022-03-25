from dataclasses import dataclass
from typing import List

@dataclass
class PathPoint:
	pass

@dataclass
class Path:
	"""An element which connects one point to another using a series of :class:`PathPoint`'s"""
	path: List[PathPoint]
	"""The path this elements connects to"""
