from dataclasses import dataclass
import math
from typing import Self, Sequence, override
from form import Form

@dataclass
class Point(Form):
    x: float
    y: float

    def distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    @override # since python 3.12 
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    def dummy(self):
        print(f'Dummy point (in real life: {type(self)})')

    # @staticmethod # no extra args
    @classmethod
    def from_coordinates(cls, coords: Sequence[float]) -> Self:  # Self since python 3.11
    #def from_coordinates(cls, coords: Sequence[float]) -> 'Point':
        if len(coords) != 2:
            raise ValueError("need 2 coordinates exactly")
        return cls("?", coords[0], coords[1])

