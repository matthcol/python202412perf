from dataclasses import dataclass
from typing import override
from point import Point

@dataclass
class WeightedPoint(Point):
    weight: float = 1.0

    @override
    def dummy(self):
        print(f'Dummy weighted point (in real life: {type(self)})')
        