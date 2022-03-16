from dataclasses import dataclass


@dataclass
class Colour:
    """
    A simple colour as used everywhere in the program. Don't use any system-specific colours for this purpose!
    
    Keyword arguments:
    red -- The value of the colour in its red spectrum, as an integer from 0 to 255
    green -- The value of the colour in its green spectrum, as an integer from 0 to 255
    blue -- The value of the colour in its blue spectrum, as an integer from 0 to 255
    alpha -- The transparancy of the colour, as an integer from 0 (transparant) to 255 (opaque)
    """
    red: int
    green: int
    blue: int
    alpha: int

    def __post_init__(self):
        self.red = int(max(0, min(255, self.red)))
        self.green = int(max(0, min(255, self.green)))
        self.blue = int(max(0, min(255, self.blue)))
        self.alpha = int(max(0, min(255, self.alpha)))

    def __eq__(self, other):
        return self.red==other.red and self.green==other.green and self.blue==other.blue and self.alpha==other.alpha