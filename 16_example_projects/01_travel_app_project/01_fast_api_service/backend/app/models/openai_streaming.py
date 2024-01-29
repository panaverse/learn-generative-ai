# models layer

from pydantic import BaseModel, model_validator
from typing_extensions import Annotated

# Validator functions
def validate_latitude(v: float) -> float:
    assert -90 <= v <= 90, 'Invalid latitude'
    return v

def validate_longitude(v: float) -> float:
    assert -180 <= v <= 180, 'Invalid longitude'
    return v

# Annotated types
Latitude = Annotated[float, validate_latitude]
Longitude = Annotated[float, validate_longitude]

# Pydantic models
class MapState(BaseModel):
    latitude: Latitude
    longitude: Longitude
    zoom: float

class MarkersState(BaseModel):
    latitudes: list[Latitude]
    longitudes: list[Longitude]
    labels: list[str]

    @model_validator(mode='after')
    def validate_marker_length(self):
        if len(self.latitudes) != len(self.longitudes) or len(self.latitudes) != len(self.labels):
            raise ValueError(
                "Latitudes, longitudes, and labels must have the same number of elements")
        return self
