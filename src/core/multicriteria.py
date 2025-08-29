"""Multicriteria scoring without pandas."""

from __future__ import annotations

from typing import Dict, List


def total_score(
    items: List[Dict[str, float]], weights: Dict[str, float]
) -> List[float]:
    total = sum(weights.values())
    scores: List[float] = []
    for it in items:
        s = sum(it[f"score_{k}"] * w for k, w in weights.items()) / total
        scores.append(s)
    return scores
