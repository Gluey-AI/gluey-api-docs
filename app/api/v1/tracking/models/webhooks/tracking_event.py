from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import MetaData, References, TrackingLevel
from app.api.v1.tracking.models.base_models import ParcelCondition, TrackingEventCodes, TrackingEventDateTime, TrackingEventDeliveryConfirmation, TrackingEventLocation, TrackingEventPhysicalData

class OtherUpdates(BaseModel):
    condition: Optional[ParcelCondition] = Field(None, description="The current condition of the parcel as reported by the carrier.")
    carrier_weight_dims: Optional[TrackingEventPhysicalData] = Field(None, description="Physical data (i.e. weight and dimensions) of the parcel that the carrier have captured whilst processing the parcel in their facilities.")
    eta: Optional[str] = Field(None, description="The estimated time of arrival as reported by the carrier in the tracking event. The date and time of the ETA is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00-05:00'", examples=['2021-06-01T12:00:00-05:00'])
    shipping_cost: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The cost of the shipment, e.g. '12.34'.")
    shipping_cost_currency: Optional[str] = Field(None, description="Available depending on carrier, if carrier provides shipping cost data. The currency of the shipping cost in ISO Alpha-3 format, e.g. 'USD', 'GBP', 'EUR' etc.")
    delivery_confirmation: Optional[TrackingEventDeliveryConfirmation] = Field(None, description="Available depending on carrier, if carrier provides delivery confirmation.")
    co2_footprint_kg: Optional[float] = Field(None, description="Available depending on carrier, if carrier provides carbon footprint data. The carbon footprint of the shipment in kg, e.g. '0.53'.")       

class TrackingEvent(BaseModel):
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="Vary depending on carrier. All additional data from the tracking event that isn't part of the Gluey standard interface.")
    event_time: TrackingEventDateTime = Field(..., description="The date and time of the tracking event when it took place.")
    codes: TrackingEventCodes = Field(..., description="The original carrier event codes and desriptions and, if used, the harmonised codes from Gluey.")
    location: TrackingEventLocation = Field(..., description="The location of the tracking event in one or more of the four main ways in which the carrier provide address information in the tracking event, e.g. carrier_location_coding, address, what3words and geo (lat, lng).")
    other: OtherUpdates = Field(None, description="Other updates various updates to the shipment / parcel that the carrier have provided.")

class TrackingEventParcel(BaseModel):
    parcel_id: str = Field(..., description="The ID of the parcel that the tracking event is related to.")
    parcel_uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel.")
    parcel_meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags that was assigned to the parcel when it was created.")
    parcel_tracking_number: str = Field(..., description="The tracking number of the parcel if available and carrier support parcel-level tracking.")
    parcel_events: list[TrackingEvent] = Field(..., description="The tracking events that have been received for the parcel.")

class TrackingData(BaseModel):
    tracking_level: TrackingLevel = Field(..., description="If tracking_level='shipment' it means the carrier does not provide parcel-level data and property 'parcel_events' will be empty. If tracking_level is 'parcel' they do provide parcel-level data and property 'parcel_events' will have data.")
    shipment_events: Optional[list[TrackingEvent]] = Field(None, description="If tracking_level='shipment'. The tracking events that have been received are on the shipment-level, i.e. individual parcels in a multi-parcel are not individually trackable.")
    parcel_events: Optional[list[TrackingEventParcel]] = Field(None, description="If tracking_level='parcel'. The tracking events that have been received a for individual parcels in the shipment.")

class TrackingWebhookEvent(BaseModel):
    shipment_id: str = Field(..., description="The ID of the shipment that the tracking event is related to.")
    shipment_uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the shipment.")
    shipment_meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags that was assigned to the shipment when it was created.")
    shipment_references: References = Field(..., description="The references of the shipment.")
    shipment_tracking_number: Optional[str] = Field(None, description="The tracking number of the shipment.")
    tracking_data: TrackingData = Field(..., description="All the tracking events received for the shipment or parcels.")