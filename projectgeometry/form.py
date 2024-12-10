
# file form.py: module form

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Form(ABC):
    name: str

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        """translate this form with relative offsets
        
        arguments:
        - delta_x[float]: horizontal relative offset
        - delta_y[float]: vertical relative offset
        """
