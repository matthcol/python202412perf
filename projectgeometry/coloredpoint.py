from dataclasses import dataclass
from typing import override
from point import Point

@dataclass
class ColoredPoint(Point):
    color: str = 'red'

    def __str__(self):
        return f"{super().__str__()}@{self.color}"

    @override
    def dummy(self):
        print(f'Dummy colored point (in real life: {type(self)})')