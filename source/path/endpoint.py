from dataclasses import dataclass
from decimal import Decimal
from typing import TypeVar, Generic
from base import Position
from shape import Shape

class EndPoint(Position):
	""" A position that terminates a line """
	pass
	
	
CuttedObject = TypeVar('CuttedObject')
	
@dataclass
class Cut(Generic[CuttedObject], Position):
	""" A position that lies on an object's path """
	parent: CuttedObject
	""" The object this instance cuts """
	
	cutPosition: Decimal
	""" The position of the cut inside this instance, as a decimal from 0 (start of the shape's path) to 1 (end of the shape's path)"""
	
	@property
	def x(self) -> Decimal:
		"""It's position on the horizontal axis"""
		return self.parent[self.cutPosition].x
	
	@property
	def y(self) -> Decimal:
		"""It's position on the vertical axis"""
		return self.parent[self.cutPosition].y
