from dataclasses import dataclass
from typing import List
from base.implementers import HasParent
from path import Path
from path.endpoint import Cut
from . import Shape
from line.extension import Ferry, Bridge

@dataclass
class Tongue(Shape, HasParent[Path]):
	"""A :class:`Tongue` is a :class:`Shape` that splits a :class:`path.Path`, from a :class:`path.endpoint.Cut` on it's sub-:class:`path.Path`'s to another :class:`path.endpoint.Cut`

..	image:: /../documentation/img/Tongue.svg
	"""
	
	startPoint: Cut[Path]
	"""The start point of the outwards line, as a :class:`path.endpoint.Cut` on any :class:`path.Path`. Contains cut styling."""
	
	endPoint: Cut[Path]
	"""The end point of the outwards line, as a :class:`path.endpoint.Cut` on any :class:`path.Path`. Contains cut styling."""
	
