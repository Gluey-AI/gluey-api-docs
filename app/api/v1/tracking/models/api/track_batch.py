
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import References, TrackingLevel
from app.api.v1.tracking.models.api.tracking_event import TrackingData, TrackingEventParcel

class BatchTrackShipment(BaseModel):
    id: str = Field(..., description="The ID of the shipment that the tracking event is related to.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the shipment.")
    tracking_level: TrackingLevel = Field(..., description="On what level tracking events are available for this shipment, if tracking_level is 'shipment' it means the carrier does not provide parcel-level data. If tracking_level is 'parcel' they do provide parcel-level data.")
    references: References = Field(..., description="The references of the shipment.")
    parcels: list[TrackingEventParcel] = Field([], description="All the parcels included in the shipment.")
    tracking_data: Optional[TrackingData] = Field(None, description="Available if tracking_level = 'shipment'. The tracking data for the shipment.")