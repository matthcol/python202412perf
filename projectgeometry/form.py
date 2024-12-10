
# file form.py: module form

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Form(ABC):
    name: str = field(compare=False) # name is ignored with ==, !=, <, <=, >=, >

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        """translate this form with relative offsets
        
        arguments:
        - delta_x[float]: horizontal relative offset
        - delta_y[float]: vertical relative offset
        """
