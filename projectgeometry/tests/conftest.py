import pytest
from geo import Point


@pytest.fixture
def point_a() -> Point:
    return Point("A", 4.25, 12.5)