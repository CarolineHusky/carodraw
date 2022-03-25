from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Position:
	"""A position in space"""
	
	x: Decimal
	"""It's position on the horizontal axis"""
	
	y: Decimal
	"""It's position on the vertical axis"""
