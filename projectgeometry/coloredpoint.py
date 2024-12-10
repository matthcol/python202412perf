from dataclasses import dataclass
from typing import override
from point import Point

@dataclass
class ColoredPoint(Point):
    color: str = 'red'

    @override
    def dummy(self):
        print(f'Dummy colored point (in real life: {type(self)})')