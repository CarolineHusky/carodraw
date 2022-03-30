from dataclasses import dataclass
from typing import List
from base.implementers import HasParent
from path import Path
from path.endpoint import Cut
from . import Shape
from line.extension import Ferry, Bridge
	

@dataclass
class Split(Shape, HasParent[Shape]):
	"""A :class:`Split` is a :class:`Tongue` that splits a :class:`Shape`, from a :class:`path.endpoint.Cut` on it's sub-:class:`Shape`'s to another :class:`path.endpoint.Cut`

..	image:: /../documentation/img/Split.svg
	"""
	
	startPoint: Cut[Shape]
	"""The start point of the outwards line, as a :class:`path.endpoint.Cut` on any :class:`Shape`. Contains cut styling."""
	
	endPoint: Cut[Shape]
	"""The end point of the outwards line, as a :class:`path.endpoint.Cut` on any :class:`Shape`. Contains cut styling."""
	
