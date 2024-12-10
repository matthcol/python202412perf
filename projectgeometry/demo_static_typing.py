from point import Point
from weightedpoint import WeightedPoint


p = Point(name='F', x=0.0, y=7.0)
p.add_inplace(3.5)
p.add_inplace(3)
p.add_inplace((1, 2))
p.add_inplace((1.0, 2.5))
p.add_inplace([1, 2.5])
#p.add_inplace([1, 2.5, 3]) # static ok, dynamic ko
p.add_inplace(Point('Z', 1.0, -1.0))
p.add_inplace(WeightedPoint('Y', 1.0, -1.0, weight=4.0))
print(p)