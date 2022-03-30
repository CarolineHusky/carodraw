from dataclasses import dataclass
from typing import List, Tuple
from base import Position
from decimal import Decimal

@dataclass
class PathPoint(Position):
	""" A position inside a path """
	pass
	
@dataclass
class CompositePathPointElement:
	percentage: Decimal
	""" The percentage this composite pathpoint element contributes to the final value"""
	
	base: PathPoint
	""" The child item"""
	
	def __getattr__(self, name):
		""" Attempts to resolve an attribute inside the element, by multiplying it by the exact amount it contributes to the composite path point """
		return getattr(self.base, name)*self.percentage
		
	
@dataclass
class CompositePathPoint:
	""" A position inside a path as calculated by an indexing of this path """
	elements: List[CompositePathPointElement]
	""" The list of elements inside this composite path point"""
	
	def __getattr__(self, name):
		""" Attempts to resolve an attribute inside the elements from a composite path point """
		# First, attempt to see if all elements internally share the same value for the key
		value = getattr(self.elements[0].base, name)
		for element in self.elements:
			if getattr(element.base, name)!=value:
				break
		else:
			return value
			
		# Secondly, if that ain't the case, average this value among the elements, using the percentage inside the compositePathPoint
		value = getattr(self.elements[0], name)
		for element in self.elements[1:]:
			value+=getattr(self.elements, name)
		return value

@dataclass
class Path:
	"""An element which connects one point to another using a series of :class:`PathPoint`'s"""
	path: List[PathPoint]
	"""The path this elements connects to"""
	
	def __len__(self):
		"""The length of a base path is always normalised to 1"""
		return 1
		
	def __length_hint__(self):
		"""The length of a base path is always normalised to 1"""
		return 1
	
	def __getitem__(self, indice):
		"""Get a representation of a position on a path"""
		if len(self.path) == 1: # Special case: we can't interpolate on a 1-point path, as silly as that might be
			return self.path[0]
			
		position = (len(self.path)-2)*indice
		return CompositePathPoint([
			CompositePathPointElement(position-int(position), self.path[int(position)]),
			CompositePathPointElement(1-(position-int(position)), self.path[int(position)+1])
			])
