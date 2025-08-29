"""Dynamic segmentation without pandas."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class Segment:
    pk_from: float
    pk_to: float


def segment_by_delta(
    points: Iterable[tuple[float, float]], delta: float, min_len: float
) -> List[Segment]:
    pts = list(points)
    segs: List[Segment] = []
    start_pk, start_val = pts[0]
    last_pk = start_pk
    for pk, val in pts[1:]:
        if abs(val - start_val) >= delta and pk - start_pk >= min_len:
            segs.append(Segment(start_pk, pk))
            start_pk = pk
            start_val = val
        last_pk = pk
    segs.append(Segment(start_pk, last_pk))
    return segs
