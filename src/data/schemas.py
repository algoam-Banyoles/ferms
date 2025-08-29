
"""DataFrame schemas using pandera."""

from __future__ import annotations

import pandera as pa
from pandera.typing import Series


class AxisSchema(pa.SchemaModel):
    pk: Series[float]
    x_utm: Series[float]
    y_utm: Series[float]

    class Config:
        strict = True


class MeasuresSchema(pa.SchemaModel):
    road_id: Series[str]
    pk: Series[float]
    metric: Series[str]
    value: Series[float]

    class Config:
        strict = True

