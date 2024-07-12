from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import MetaData
from app.api.v1.tracking.models.base_models import ParcelCondition, TrackingEventCodes, TrackingEventDateTime, TrackingEventDeliveryConfirmation, TrackingEventLocation, TrackingEventPhysicalData

class TrackingEvent(BaseModel):
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="Vary depending on carrier. All additional data from the tracking event that isn't part of the Gluey standard interface.")
    event_time: TrackingEventDateTime = Field(..., description="The date and time of the tracking event when it took place.")
    eta: Optional[str] = Field(None, description="The estimated time of arrival as reported by the carrier in the tracking event. The date and time of the ETA is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00-05:00'", examples=['2021-06-01T12:00:00-05:00'])
    codes: TrackingEventCodes = Field(..., description="The original carrier event codes and desriptions and, if used, the harmonised codes from Gluey.")
    location: TrackingEventLocation = Field(..., description="The location of the tracking event in one or more of the four main ways in which the carrier provide address information in the tracking event, e.g. carrier_location_coding, address, what3words and geo (lat, lng).")

class TrackingData(BaseModel):
    current_eta: Optional[str] = Field(None, description="If carrier provides an ETA (estimated time of arrival), this is the last ETA update from the carrier. The date and time of the ETA is in ISO 8601 format and includes the UTC-offset, '2021-06-01T12:00:00-05:00'.", examples=['2021-06-01T12:00:00-05:00'])
    shipping_cost: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The cost of the shipment, e.g. '12.34'.")
    shipping_cost_currency: Optional[str] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The currency of the shipping cost in ISO Alpha-3 format, e.g. 'USD', 'GBP', 'EUR' etc.")
    delivery_confirmation: Optional[TrackingEventDeliveryConfirmation] = Field(None, description="Available depending on carrier, if carrier provides delivery confirmation.")
    co2_footprint_kg: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides carbon footprint data. The carbon footprint of the shipment in kg, e.g. '0.53'.")   
    events: Optional[list[TrackingEvent]] = Field([], description="Available depending on carrier, if carrier support parcel-level tracking event. Otherwise shipment-level events will be provided.")

class TrackingEventParcel(BaseModel):
    id: str = Field(..., description="The ID of the parcel that the tracking event is related to.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Meta data tags you assigned when it was created in Gluey.")
    carrier_tracking_id: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. This is the carriers own tracking id for the parcel")
    condition: ParcelCondition = Field(ParcelCondition.UNKNOWN, description="The current condition of the parcel as reported by the carrier.")
    carrier_weight_dims: Optional[TrackingEventPhysicalData] = Field(None, description="Physical data (i.e. weight and dimensions) of the parcel that the carrier have captured whilst processing the parcel in their facilities.")
    tracking_data: Optional[TrackingData] = Field(None, description="Available if `tracking_level=parcel`. The tracking data for the individual parcel.")