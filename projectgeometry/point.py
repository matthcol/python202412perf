from dataclasses import dataclass
import math
from form import Form

@dataclass
class Point(Form):
    x: float
    y: float

    def distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)