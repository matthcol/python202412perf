from copy import copy
import pytest
from geo import Point

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


@pytest.mark.parametrize(
        "sequence",
        [
            (),
            (2.5,),
            (2.5, 4.5, 7.5),
        ],
        ids=[
            "empty sequence",
            "sequence size 1",
            "sequence size 3",
        ]
)
def test_from_coordinates_ko(sequence):
    with pytest.raises(ValueError) as ex_info:
        # auto: ex_info.__enter__()
        _ = Point.from_coordinates(sequence)
        # auto: ex_info.__exit__()
    assert "need 2 coordinates exactly" == str(ex_info.value) 
    # NB: ex_info is a wrapper, ex_info.value contains the captured exception (ValueError)


def test_eq_same(point_a):
    assert point_a == point_a

def test_eq_copy(point_a):
    point_a_copy = copy(point_a)
    # assert point_a_copy is not point_a # we have 2 different objects in memory
    assert point_a == point_a_copy

def test_eq_same_coords_different_name(point_a):
    point_b = Point('b', point_a.x, point_a.y)
    assert point_a == point_b

# ("A", 4.25, 12.5)
@pytest.mark.parametrize(
     "name, x, y",
     [
         ('A', 1.0, 12.5),
         ('A', 4.25, -1.0),
         ('A', 1.0, -1.0),
         ('B', 1.0, 12.5),
         ('B', 4.25, -1.0),
         ('B', 1.0, -1.0),
     ]   
)
def test_eq_ko(point_a, name, x, y):
    point_b = Point(name, x, y)
    assert not (point_a == point_b)