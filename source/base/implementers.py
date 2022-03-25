from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Generator, TypeVar, Generic

Parent = TypeVar('Parent')

@dataclass
class HasParent(Generic[Parent]):
	"""The typing for a class that has a parent, and hence an origin"""
	
	parent: Union[HasParent,Parent]
	"""This is the direct ancestor of the element"""
	
	@property
	def antecedants(self) -> Generator[Union[HasParent,Parent]]:
		"""The list of antecedants of the element"""
		parent = self
		while isinstance(parent, HasParent):
			parent = parent.parent
			yield parent
			
	@property
	def origin(self) -> Parent:
		"""The parent at the very most origin of this element"""
		*_, last = antecedants
		return last


@dataclass
class HasOtherParent(Generic[Parent]):
	"""The typing for a class that has another parent, and hence another origin"""
	
	otherParent: Union[HasOtherParent,Parent]
	"""This is the other direct ancestor of the element"""
	
	@property
	def otherAntecedants(self) -> Generator[Union[HasOtherParent,Parent]]:
		"""The other list of antecedants of the element"""
		parent = self
		while isinstance(parent, HasOtherParent):
			parent = parent.otherParent
			yield parent
			
	@property
	def otherOrigin(self) -> Parent:
		"""The other parent at the very most origin of this element"""
		*_, last = antecedants
		return last
