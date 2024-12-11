from dataclasses import dataclass
from typing import override
from geo.model.point import Point

@dataclass
class WeightedPoint(Point):
    weight: float = 1.0

    def __str__(self):
        return f"{super().__str__()}#{self.weight}"

    @override
    def dummy(self):
        print(f'Dummy weighted point (in real life: {type(self)})')
        