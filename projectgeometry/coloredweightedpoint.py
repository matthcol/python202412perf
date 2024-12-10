from dataclasses import dataclass

from coloredpoint import ColoredPoint
from weightedpoint import WeightedPoint


@dataclass
class ColoredWeightedPoint(ColoredPoint, WeightedPoint):
    pass