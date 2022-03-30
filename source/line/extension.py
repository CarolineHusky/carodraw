from path import Path
from path.endpoint import EndPoint, Cut
from dataclasses import dataclass
from . import Line
from shape import Shape
from base.implementers import HasParent, HasOtherParent

@dataclass
class Outwards(Line, HasParent[Path]):
	"""An `Outwards` is a :class:`line.Line` that has its :attr:`startPoint` on a `Cut` of the :class:`path.Path`, and which goes outwards from that `Path` from it until it reach its own :attr:`endPoint`

..	image:: /../documentation/img/Outwards.svg
	"""
	
	startPoint: Cut[Path]
	"""The start point of the outwards line, as a `Cut` on any `Path`. Contains cut styling."""


@dataclass
class Inwards(Outwards, HasParent[Shape]):
	"""An `Inwards` is an :class:`Outwards` on a `Shape` that goes inwards to its shape
	
..	image:: /../documentation/img/Inwards.svg
	"""
	
	startPoint: Cut[Shape]
	"""The start point of the outwards line, as a `Cut` on any `Shape`. Contains cut styling."""
	
	
@dataclass
class Ferry(Outwards, HasOtherParent[Path]):
	"""A `Ferry` is a :class:`Outwards` that ends in another :class:`path.Path`
	
..	image:: /../documentation/img/Ferry.svg
	"""
	
	endPoint: Cut[Path]
	"""The end point of the outwards line, as a `Cut` on any `Path`. Contains cut styling."""
	
		
@dataclass
class Bridge(Inwards, HasOtherParent[Shape]):
	"""A `Bridge` is a :class:`Inwards` that ends in another :class:`shape.Shape`
	
..	image:: /../documentation/img/Bridge.svg
	"""
	
	endPoint: Cut[Shape]
	"""The end point of the outwards line, as a `Cut` on any `Shape`. Contains cut styling."""
