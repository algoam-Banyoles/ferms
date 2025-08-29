"""Coordinate reference system utilities."""

from __future__ import annotations

from pyproj import Transformer

DEFAULT_CRS = "EPSG:25831"


def build_transformer(src: str, dst: str = DEFAULT_CRS) -> Transformer:
    """Return a pyproj Transformer from src to dst CRS."""
    return Transformer.from_crs(src, dst, always_xy=True)
