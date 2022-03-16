from typing import Any, Union, Dict, Generic, List, TypeVar


class AmbiguousPositionalException(Exception):
    """Exception for when a positional argument couldn't be resolved"""
    def __init__(self, name) -> None:
        super().__init__("Cannot resolve positional argument '%s' without a provided position"%name)


SetVar = TypeVar('SetVar')


class PositionalSampling(Generic[SetVar], SetVar):
    """
    A sampling of a set of properties that vary along space
    
    Arguments:
    samples -- A dictionary mapping each sample to it's percentage of contribution to the final result
    """
    def __init__(self, samples: Dict[Generic[SetVar], float]):
        self.samples = samples

    def __getattr__(self, name: str):
        """Interpolates between the different values"""
        value = None
        for ele in self.samples:
            sample = getattr(ele, name) * self.samples[ele]
            if value==None:
                value = sample
            else:
                value += sample
        return value


class Positional(Generic[SetVar], SetVar):
    circle: bool = False

    """A set of properties that vary along space"""
    def __init__(self, values: List[SetVar]):
        self.values = values

    def __getattr__(self, name: str):
        """Attempts to resolve a positional property without a position. Fails if not all positionals have the same value for it"""
        if self.values==None or self.values==[]:
            raise IndexError()
        value=getattr(self.values[0], name)
        for element in self.values:
            if getattr(element, name) != value:
                raise AmbiguousPositionalException(name)
        return value

    def __setattr__(self, __name: str, __value: Any) -> None:
        """Sets a value for all positionals"""
        if(__name not in SetVar.__dict__):
            super().__setattr__(__name, __value)
        else:
            for ele in self.values:
                setattr(ele, __name, __value)

    def __getitem__(self, position: Union[int,float]) -> Union[SetVar, PositionalSampling[SetVar]]:
        if position<0 and not self.circle:
            return self.values[0]
        if type(position)==int:
            if position>len(self.values) and not self.circle:
                return self.values[-1]
            return self.values[position%len(self.values)]
        if position>1 and not self.circle:
            return self.values[-1]
        position%=1
        if self.values==None or self.values==[]:
            raise IndexError()
        position*=len(self.values)
        if int(position)==position:
            return self.values[position]
        first_sample = self.values[int(position)]
        second_sample = self.values[int(position)+1]
        return PositionalSampling(self, {first_sample: 1-(position-int(position)), second_sample: position-int(position)})

