from dataclasses import dataclass
from typing import TypeVar, Generic

class StyledEndPoint:
	pass
	
	
CuttedObject = TypeVar('CuttedObject')
	
@dataclass
class StyledCut(Generic[CuttedObject]):
	parent: CuttedObject

