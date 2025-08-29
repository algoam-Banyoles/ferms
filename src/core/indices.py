"""Indicator normalisation and composite indices without pandas."""

from __future__ import annotations

from typing import Dict, List, Union


def norm_iri(v: float) -> float:
    return max(0.0, min(100.0, 100 - 25 * v))


def norm_rd(v: float) -> float:
    return max(0.0, min(100.0, 100 - 50 * v))


def norm_sfc(v: float) -> float:
    return max(0.0, min(100.0, v * 100))


def norm_mpd(v: float) -> float:
    return max(0.0, min(100.0, 100 - abs(v - 0.8) / 0.8 * 100))


def norm_fwd(v: float) -> float:
    return max(0.0, min(100.0, 100 - v * 10))


NORMALIZERS = {
    "IRI": norm_iri,
    "RD": norm_rd,
    "SFC": norm_sfc,
    "MPD": norm_mpd,
    "FWD": norm_fwd,
}


Measure = Dict[str, Union[str, float]]


def compute_indices(measures: List[Measure]) -> List[Measure]:
    """Add normalised score to a list of measure dicts."""
    out: List[Measure] = []
    for m in measures:
        metric = str(m["metric"])
        value = float(m["value"])
        score = NORMALIZERS[metric](value)
        out.append({**m, "score": score})
    return out


def composite_indices(values: Dict[str, float], weights: Dict[str, float]) -> float:
    """Compute weighted composite index."""
    total = sum(weights.values())
    return sum(values[k] * w for k, w in weights.items()) / total
