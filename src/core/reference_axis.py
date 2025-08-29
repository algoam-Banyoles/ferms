"""Reference axis handling without shapely."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List, Tuple


@dataclass
class AxisSegment:
    start_pk: float
    end_pk: float
    ax: float
    ay: float
    bx: float
    by: float

    def length(self) -> float:
        return math.hypot(self.bx - self.ax, self.by - self.ay)


@dataclass
class ReferenceAxis:
    segments: List[AxisSegment]

    @classmethod
    def from_points(cls, pts: Iterable[Tuple[float, float, float]]) -> "ReferenceAxis":
        pts_sorted = sorted(pts, key=lambda p: p[0])
        segments: List[AxisSegment] = []
        for (pk1, x1, y1), (pk2, x2, y2) in zip(pts_sorted[:-1], pts_sorted[1:]):
            segments.append(AxisSegment(pk1, pk2, x1, y1, x2, y2))
        return cls(segments)

    def length(self) -> float:
        return sum(seg.length() for seg in self.segments)
