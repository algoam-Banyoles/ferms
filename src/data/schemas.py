from pandera import SchemaModel
from pandera.typing import Series


class AxisSchema(SchemaModel):
    """Schema for axis data."""
    x: Series[int]
    y: Series[int]


class MeasuresSchema(SchemaModel):
    """Schema for measurement data."""
    length: Series[float]
    width: Series[float]
