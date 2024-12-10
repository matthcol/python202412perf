from dataclasses import dataclass

from coloredpoint import ColoredPoint
from weightedpoint import WeightedPoint


@dataclass
class ColoredWeightedPoint(ColoredPoint, WeightedPoint):
    pass

    def dummy(self):
        super().dummy()
        print(f'Dummy colored weighted point (in real life: {type(self)})')

    def dummy_c(self):
        ColoredPoint.dummy(self)
        
    def dummy_w(self):
        WeightedPoint.dummy(self)