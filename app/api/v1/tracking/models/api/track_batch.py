
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import References, TrackingLevel, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.tracking.models.api.tracking_event import TrackingData, TrackingEventParcel

class BatchTrackShipment(BaseModel):
    id: str = Field(..., description="The ID of the shipment that the tracking event is related to.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the shipment.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    references: References = Field(..., description="The references of the shipment.")
    parcels: list[TrackingEventParcel] = Field([], description="All the parcels included in the shipment.")
    tracking_data: Optional[TrackingData] = Field(None, description="Available if tracking_level = 'shipment'. The tracking data for the shipment.")