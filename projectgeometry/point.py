from dataclasses import dataclass
import math
import typing
from typing import Self, override
from collections import abc
from form import Form

@dataclass(order=True)
class Point(Form):
    x: float
    y: float

    def __str__(self):
        return f"{self.name}({self.x}, {self.y})"
    
    # static typing
    def add_inplace(self, other:float|int|typing.Sequence[float|int]|'Point'):
        self += other

    # dynamic typing
    def __iadd__(self, other):
        if isinstance(other, (float, int)):
            self.translate(other, other)
        elif isinstance(other, abc.Sequence):
            self.translate(*other)
            # NB1: unpack sequence other into positional args
            # NB2: number of arguments is verified during unpack
            # NB3: values of sequence will be verified by duck typing
        elif isinstance(other, Point):
            self.translate(other.x, other.y)
        else:
            return NotImplemented
        return self

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
    def from_coordinates(cls, coords: typing.Sequence[float]) -> Self:  # Self since python 3.11
    #def from_coordinates(cls, coords: Sequence[float]) -> 'Point':
        if len(coords) != 2:
            raise ValueError("need 2 coordinates exactly")
        return cls("?", coords[0], coords[1])

