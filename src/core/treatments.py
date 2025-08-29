"""Treatment rules handling."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Treatment:
    treat_id: int
    name: str
    cost_eur_m2: float
    life_years: float
    co2_kg_m2: float
    rules: Dict


class Bank:
    def __init__(self, treatments: List[Treatment]):
        self.treatments = treatments

    def select(self, ctx: Dict) -> Optional[Treatment]:
        for tr in self.treatments:
            cond = tr.rules.get("metric")
            if cond is None:
                return tr
            metric = ctx.get(cond["name"])  # e.g. idx_global
            if metric is None:
                continue
            lo, hi = cond.get("range", (0, 100))
            if lo <= metric <= hi:
                return tr
        return None
