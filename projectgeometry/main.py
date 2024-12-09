
from form import Form
from point import Point


pA = Point('A', 1.0, 2.5)
pB = Point(name='B', x=4.0, y=6.5)

for p in pA, pB:
    print(p)
    print(p.name, p.x, p.y)
    print()

assert isinstance(pA, Point)
assert isinstance(pA, Form)
assert isinstance(pA, object)

print('MRO class Form:', Form.mro())
print('MRO class Point:', Point.mro())

print()
d = pA.distance(pB)
print(f"distance between {pA} and {pB} is {d}")

# d = pA.distance('123')
# print(d)