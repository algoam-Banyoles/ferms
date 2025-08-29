"""Reporting helpers."""

from __future__ import annotations

from typing import Iterable


def total_co2(segments: Iterable[dict]) -> float:
    """Sum CO2 from segment dictionaries with 'co2' keys."""
    return sum(seg.get("co2", 0.0) for seg in segments)
