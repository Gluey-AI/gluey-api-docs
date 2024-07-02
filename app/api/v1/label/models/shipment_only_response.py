from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.api.v1.common.models.base_models import TrackingLevel
from app.api.v1.label.models.base_models import ManifestStatus

class ItemOnlyResponseModel(BaseModel):
    """Class representing an item included in each parcel."""
    id: str = Field(..., description="The unique identifier for the item.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")

class ParcelOnlyResponseModel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="The unique identifier for the parcel. If not provided, Gluey will generate a unique identifier.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel. This will be included in subsequent messages such as tracking events, label responses etc.")
    items: Optional[list[ItemOnlyResponseModel]] = Field([], description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class ShipmentOnlyResponseModel(BaseModel):
    """Class representing a shipment containing multiple parcels."""
    id: str = Field(..., description="The unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment. This will be included in subsequent messages such as tracking events and can be used to identify the shipment in your own system.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    updated_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was last updated in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    tracking_level: TrackingLevel = Field(..., description="The tracking level of the shipment. This indicates if the shipment is tracked at parcel level, shipment level. For shipments with multiple parcels, the parcels are only individually trackable when tracking-level is 'parcel'.")
    manifest_status: ManifestStatus = Field(..., description="The manifest status of the shipment. This indicates if the shipment needs to be manifested with carrier, if Gluey is handling it in the background, if it is not needed, or if it has been done.")
    parcels: list[ParcelOnlyResponseModel] = Field([], description="A list of parcels included in the shipment")