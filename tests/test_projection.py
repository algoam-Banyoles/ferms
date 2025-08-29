import pytest

from src.core.projection import project_points
from src.core.reference_axis import ReferenceAxis


def test_projection_basic():
    axis = ReferenceAxis.from_points([(0, 0, 0), (100, 100, 0)])
    pts = [(10, 10), (50, 0)]
    res = project_points(axis, pts)
    assert res[0]["pk"] == pytest.approx(10, abs=1e-6)
    assert res[1]["pk"] == pytest.approx(50, abs=1e-6)
