"""Projection of points onto reference axis without shapely."""

from __future__ import annotations

import math
from typing import Iterable, List, Tuple

from .reference_axis import ReferenceAxis


def project_points(
    axis: ReferenceAxis, pts: Iterable[Tuple[float, float]]
) -> List[dict]:
    results: List[dict] = []
    for x, y in pts:
        best = None
        for seg in axis.segments:
            ax, ay, bx, by = seg.ax, seg.ay, seg.bx, seg.by
            abx = bx - ax
            aby = by - ay
            apx = x - ax
            apy = y - ay
            ab2 = abx * abx + aby * aby
            if ab2 == 0:
                t = 0.0
            else:
                t = (apx * abx + apy * aby) / ab2
            t = max(0.0, min(1.0, t))
            qx = ax + t * abx
            qy = ay + t * aby
            dist = math.hypot(x - qx, y - qy)
            pk = seg.start_pk + (seg.end_pk - seg.start_pk) * t
            if best is None or dist < best[0]:
                best = (dist, pk)
        if best is None:
            raise ValueError("axis has no segments")
        results.append({"pk": best[1], "distance": best[0]})
    return results
