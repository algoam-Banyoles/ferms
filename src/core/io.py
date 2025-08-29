"""Input/output helpers."""

from __future__ import annotations

import pandas as pd

from ..data import schemas


def read_axis(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    schemas.AxisSchema.validate(df)
    return df


def read_measures(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    schemas.MeasuresSchema.validate(df)
    return df
