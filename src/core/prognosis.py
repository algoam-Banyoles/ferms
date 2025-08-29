"""Simple deterioration models."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List


@dataclass
class LinearPiecewise:
    y0: float
    k1: float
    k2: float
    switch: int

    def predict(self, years: List[int]) -> List[float]:
        out = []
        for t in years:
            if t <= self.switch:
                out.append(self.y0 + self.k1 * t)
            else:
                y_switch = self.y0 + self.k1 * self.switch
                out.append(y_switch + self.k2 * (t - self.switch))
        return out


@dataclass
class Gompertz:
    a: float
    b: float
    c: float

    def predict(self, years: List[int]) -> List[float]:
        return [self.a * math.exp(-self.b * math.exp(-self.c * t)) for t in years]
