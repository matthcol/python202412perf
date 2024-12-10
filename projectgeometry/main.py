
from coloredpoint import ColoredPoint
from form import Form
from point import Point
from weightedpoint import WeightedPoint
from coloredweightedpoint import  ColoredWeightedPoint


def play_with_points():
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

def play_with_specialized_points():
    print("**** PLAY WITH SPECIALIZED POINTS ****")
    p_a = Point('A', 1.5, 2.5)
    wp_b = WeightedPoint('B', 4.5, 5.5, weight=12.75)
    cp_c = ColoredPoint('C', 6.5, 7.5, color='red')
    cwp_d = ColoredWeightedPoint('D', 8.5, 12.25, weight=10.25, color='green')
    points = [p_a, wp_b, cp_c, cwp_d]
    for p in points:
        print('*', p.name)
        print('\t- str:', p)
        print('\t- coords:', p.x, p.y)
        print('\t- distance from A:', p.distance(p_a))

    print('MRO class Point:', Point.mro())
    print('MRO class WeightedPoint:', WeightedPoint.mro())
    print('MRO class ColoredPoint:', ColoredPoint.mro())
    print('MRO class ColoredWeightedPoint:', ColoredWeightedPoint.mro())

if __name__ == '__main__':
    play_with_points()
    print()
    play_with_specialized_points()