from dataclasses import dataclass
from point import Point

@dataclass
class WeightedPoint(Point):
    weight: float

    def dummy(self):
        print(f'Dummy weighted point (in real life: {type(self)})')
        