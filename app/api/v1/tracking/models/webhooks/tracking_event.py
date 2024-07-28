from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import MetaData, References, TrackingLevel, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.tracking.models.base_models import ParcelCondition, TrackingEventCodes, TrackingEventDateTime, TrackingEventDeliveryConfirmation, TrackingEventLocation, TrackingEventPhysicalData

class OtherUpdates(BaseModel):
    condition: Optional[ParcelCondition] = Field(None, description="The current condition of the parcel as reported by the carrier.")
    carrier_weight_dims: Optional[TrackingEventPhysicalData] = Field(None, description="Physical data (i.e. weight and dimensions) of the parcel that the carrier have captured whilst processing the parcel in their facilities.")
    eta: Optional[datetime] = Field(None, description="The estimated time of arrival as reported by the carrier in the tracking event. The date and time of the ETA is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00-05:00'", examples=['2021-06-01T12:00:00-05:00'])
    shipping_cost: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The cost of the shipment, e.g. '12.34'.")
    shipping_cost_currency: Optional[str] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The currency of the shipping cost in ISO Alpha-3 format, e.g. 'USD', 'GBP', 'EUR' etc.")
    delivery_confirmation: Optional[TrackingEventDeliveryConfirmation] = Field(None, description="Available depending on carrier, if carrier provides delivery confirmation.")
    co2_footprint_kg: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides carbon footprint data. The carbon footprint of the shipment in kg, e.g. '0.53'.")       

class TrackingEvent(BaseModel):
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="Vary depending on carrier. All additional data from the tracking event that isn't part of the Gluey standard interface.")
    event_time: TrackingEventDateTime = Field(..., description="The date and time of the tracking event when it took place.")
    codes: TrackingEventCodes = Field(..., description="The original carrier event codes and desriptions and, if used, the harmonised codes from Gluey.")
    location: TrackingEventLocation = Field(..., description="The location of the tracking event in one or more of the four main ways in which the carrier provide address information in the tracking event, e.g. carrier_location_coding, address, what3words and geo (lat, lng).")
    other: Optional[OtherUpdates] = Field(None, description="Other updates various updates to the shipment / parcel that the carrier have provided.")

class TrackingEventParcel(BaseModel):
    carrier_tracking_id: str = Field(None, description="This is the carriers own tracking id for the parcel")
    parcel_id: str = Field(..., description="Glueys ID of the parcel that the tracking event is related to.")
    parcel_uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel, if assigned during shipment creation.")
    parcel_meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags that was assigned to the parcel when the shipment was created.")

class TrackingWebhookEvent(BaseModel):
    shipment_id: str = Field(..., description="The Gluey ID of the shipment that the tracking event is related to.")
    shipment_uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the shipment.")
    shipment_meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags that was assigned to the shipment when it was created.")
    carrier_id: str = Field(..., description="The ID of the carrier that the shipment is associated with.")
    carrier_tracking_id: str = Field(..., description="This is the carriers own tracking id for the shipment.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    parcel: Optional[TrackingEventParcel] = Field(None, description="Only available when `tracking_level=parcel`. For multi-parcel shipments this means that this is a reference to the an individual parcel the tracking event is associated with.")
    event: TrackingEvent = Field(..., description="The tracking event that have been received for the shipment.")