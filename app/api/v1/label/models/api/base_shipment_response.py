from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from app.api.v1.common.models.base_models import MetaData, TrackingLevel, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.base_models import ManifestStatus, manifest_status_descriptions

class BaseItemResponseModel(BaseModel):
    """Class representing an item included in each parcel."""
    id: str = Field(..., description="Glueys own unique identifier for the item.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")

class BaseParcelResponseModel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="Glueys own unique identifier for the parcel.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel.")
    items: Optional[list[BaseItemResponseModel]] = Field([], description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class BaseShipmentResponseModel(BaseModel):
    id: str = Field(..., description="The unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    updated_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was last updated in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    manifest_status: ManifestStatus = Field(..., description=f"The manifest status of the shipment. It can be one of the following:\n{get_enum_description(ManifestStatus, manifest_status_descriptions)}")
    manifest_id: Optional[str] = Field(None, description="The Gluey manifest id related to the shipment, if applicable and shipment is manifested.")
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="Meta data received from the carrier.")
    parcels: list[BaseParcelResponseModel] = Field([], description="A list of parcels included in the shipment")