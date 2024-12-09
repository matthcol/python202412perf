from point import Point


def test_distance():
    pA = Point('A', 1.25, 2.5)
    pB = Point(name='B', x=4.25, y=6.5)
    assert 5.0 == pA.distance(pB)