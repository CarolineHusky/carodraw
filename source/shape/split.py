from dataclasses import dataclass
from typing import List
from base.implementers import HasParent
from path import Path
from path.endpoint import StyledCut
from . import Shape
from line.extension import Ferry, Bridge
	

@dataclass
class Split(Shape, HasParent[Shape]):
	"""A :class:`Split` is a :class:`Tongue` that splits a :class:`Shape`, from a :class:`base.StyledCut` on it's sub-:class:`Shape's to another :class:`path.endpoint.StyledCut`

..	image:: /../documentation/img/Split.svg
	"""
	
	startPoint: StyledCut[Shape]
	"""The start point of the outwards line, as a `Cut` on any `Shape`. Contains cut styling."""
	
	endPoint: StyledCut[Shape]
	"""The end point of the outwards line, as a `Cut` on any `Shape`. Contains cut styling."""
	
	
@dataclass
class BridgedSplit(Split):
	"""A :class:`Split` that encloses a set of other :class:`Shape`s using a :attr:`path` of :class:`Bridge`'s
	
..	image:: /../documentation/img/BridgedSplit.svg
	"""
	path: List[Bridge]
	"""The set of bridges that this split connects. Each :class:`Bridge` needs to lead back to the preceding bridge in the list, and the :attr:`Bridge.origin` of the first element in the list needs to be the :attr:`Bridge.otherOrigin` of the last element in the list"""
