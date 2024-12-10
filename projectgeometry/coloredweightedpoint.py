from dataclasses import dataclass
from typing import override

from coloredpoint import ColoredPoint
from weightedpoint import WeightedPoint


@dataclass
class ColoredWeightedPoint(ColoredPoint, WeightedPoint):

    @override
    def dummy(self):
        super().dummy()
        print(f'Dummy colored weighted point (in real life: {type(self)})')

    def dummy_c(self):
        ColoredPoint.dummy(self)
        
    def dummy_w(self):
        WeightedPoint.dummy(self)