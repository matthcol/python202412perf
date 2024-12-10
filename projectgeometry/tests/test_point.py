import pytest
from point import Point

def test_distance():
    pA = Point('A', 1.2, 4.5)
    pB = Point(name='B', x=3.4, y=5.6)
    d = pA.distance(pB)
    assert d == pytest.approx(2.45967477, 1E-8)

@pytest.mark.parametrize(
        "x1, y1, x2, y2, expected_distance, epsilon",
        [
            (2.5, 5.25, 5.5, 1.25, 5.0, 0.0),
            (2.5E300, 5.25E300, 5.5E300, 1.25E300, 5.0E300, 1E-12),
            (2.5E-300, 5.25E-300, 5.5E-300, 1.25E-300, 5.0E-300, 0.0),
        ],
        ids=[
            "median values",
            "big values",
            "small values"
        ]
)
def test_distance_345(x1, y1, x2, y2, expected_distance, epsilon):
    pA = Point('A', x1, y1)
    pB = Point(name='B', x=x2, y=y2)
    actual_distance = pA.distance(pB)
    assert expected_distance == pytest.approx(actual_distance, epsilon)


def test_translate(point_a):
    point_a.translate(1.25, -2.5)
    assert 5.5 == point_a.x
    assert 10.0 == point_a.y