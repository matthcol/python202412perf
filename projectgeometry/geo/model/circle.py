from dataclasses import dataclass
import math
from typing import override

from geo.model.form import Form
from geo.model.mesurable2d import Mesurable2D
from geo.model.point import Point


@dataclass
class Circle(Form, Mesurable2D):
    center: Point
    radius: float

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.center.translate(delta_x, delta_y)

    @override
    def surface(self) -> float:
        return math.pi * self.radius**2
    
    @override
    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius