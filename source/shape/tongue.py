from dataclasses import dataclass
from typing import List
from base.implementers import HasParent
from path import Path
from path.endpoint import StyledCut
from . import Shape
from line.extension import Ferry, Bridge

@dataclass
class Tongue(Shape, HasParent[Path]):
	"""A :class:`Tongue` is a :class:`Shape` that splits a :class:`path.Path`, from a :class:`base.StyledCut` on it's sub-:class:`path.Path's to another :class:`path.endpoint.StyledCut`

..	image:: /../documentation/img/Tongue.svg
	"""
	
	startPoint: StyledCut[Path]
	"""The start point of the outwards line, as a `Cut` on any `Path`. Contains cut styling."""
	
	endPoint: StyledCut[Path]
	"""The end point of the outwards line, as a `Cut` on any `Path`. Contains cut styling."""
	
	
@dataclass
class Dam(Tongue):
	"""A :class:`Tongue` that encloses a set of other :class:`Shape`s using a :attr:`path` of :class:`Ferry`'s
	
..	image:: /../documentation/img/Dam.svg
	"""
	path: List[Ferry]
	"""The set of ferries that this tongue connects. Each :class:`Ferry` needs to lead back to the preceding ferry in the list, and the :attr:`Ferry.origin` of the first element in the list needs to be the :attr:`Ferry.otherOrigin` of the last element in the list"""
