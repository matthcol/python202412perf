from geo.model.form import Form
from geo.model.mesurable2d import Mesurable2D


def total_surface_of_mesurable_forms(forms: list[Form]) -> float:
    return sum(f.surface() for f in forms if isinstance(f, Mesurable2D))