from dataclasses import dataclass
from point import Point

@dataclass
class ColoredPoint(Point):
    color: str

    def dummy(self):
        print(f'Dummy colored point (in real life: {type(self)})')