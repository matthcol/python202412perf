from collections.abc import Iterable, Sized
from dataclasses import dataclass, field
from typing import Iterator, override
from form import Form
from mesurable2d import Mesurable2D
from point import Point

@dataclass
class Polygon(Form, Mesurable2D, Iterable, Sized):
    """class representing a Polygon with its vertices

    NB: a polygon has at least 3 vertices
    """
    
    vertices: list[Point] = field(default_factory=list)

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        for vertix in self.vertices:
            vertix.translate(delta_x, delta_y)

    # shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    @override
    def surface(self) -> float:
        res = 0.0
        prev = self.vertices[-1]
        for current in self.vertices:
            res += prev.x * current.y - prev.y * current.x
            prev = current
        return abs(res) / 2.0
    
    @override
    def perimeter(self) -> float:
        res = 0.0
        prev = self.vertices[-1]
        for current in self.vertices:
            res += prev.distance(current)
            prev = current
        return res

    def __iter__(self) -> Iterator[Point]:
        return iter(self.vertices)

    def __len__(self) -> int:
        return len(self.vertices)


