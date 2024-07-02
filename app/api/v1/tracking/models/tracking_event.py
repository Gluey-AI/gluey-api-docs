from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Dimensions, GeoLocation, MetaData, Weight
from app.api.v1.tracking.models.base_models import ImageFormat, LocationType, ParcelCondition


class TrackingEventAddress(BaseModel):
    """Class representing an address where a tracking event took place."""
    type: Optional[LocationType] = Field(None, description="A classification of the type of location where the event took place, e.g. 'AIRPORT', 'HUB', 'DEPOT' etc.")
    name: Optional[str] = Field(None, description="The name of the location")
    street: Optional[str] = Field(None, description="The first line of the address")
    street_2: Optional[str] = Field(None, description="The second line of the address")
    postal_code: Optional[str] = Field(None, description="The postal code or ZIP code")
    suburb: Optional[str] = Field(None, description="The suburb or district. Only applicable to specific countries such as Australia and New Zealand.")
    city: Optional[str] = Field(None, description="The city or town")
    state: Optional[str] = Field(None, description="The state or province. Only applicable to specific countries such as the US, Canada, Australia etc.")
    iso_country: Optional[str] = Field(None, description="The ISO 3166-1 alpha-3 ('USA', 'GBR', 'DEU') country code.")

class CarrierLocationCode(BaseModel):
    code: str = Field(..., description="The code of the location, e.g. 'SORLHR536'")
    description: Optional[str] = Field(None, description="A description of the location code, e.g. 'Heathrow Hub'")
    type: Optional[LocationType] = Field(None, description="A classification of the type of location where the event took place, e.g. 'AIRPORT', 'HUB', 'DEPOT' etc.")

class TrackingEventLocation(BaseModel):
    """Class representing the location of a tracking event, and the four main ways in which the carrier can provide address information in the tracking event, e.g. carrier_location_coding, address, what3words and geo (lat, lng). Can be one or more available."""
    carrier_location_coding: Optional[CarrierLocationCode] = Field(None, description="A location code, and description of the location code, assigned by the carrier of where the event took place, e.g. 'SORLHR536' and 'Heathrow Hub'.")
    address: Optional[TrackingEventAddress] = Field(None, description="The address where the event took place.")
    what3words: Optional[str] = Field(None, description="The what3words location of the event, e.g. 'index.home.raft'.")
    geo: Optional[GeoLocation] = Field(None, description="The geo location of the event, e.g. '51.521251,-0.203586'.")

class TrackingEventCodeDetail(BaseModel):
    code: str = Field(..., description="The code of the tracking event, e.g. 'DEP', 'ARR', 'DLV' etc.")
    sub_code: Optional[str] = Field(None, description="The subcode of the tracking event, e.g. 'DEP-LHR', 'ARR-GTW', 'DLV-FD' etc.")
    description_code: Optional[str] = Field(None, description="A description of what the 'code' of the tracking event means, e.g. 'Departed', 'Arrived', 'Delivered' etc.")
    description_sub_code: Optional[str] = Field(None, description="A description of what the 'sub_code' of the tracking event means, e.g. 'Departed from Heathrow', 'Arrived at Gatwick', 'Delivered to front door' etc.")

class TrackingEventDateTime(BaseModel):
    created_utc: str = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the tracking event was created in the Gluey system. The date and time of the tracking event is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    carrier_utc: str = Field(..., description="Local time for the carrier when the tracking event took place. The date and time of the tracking event is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00-05:00', '2021-06-01T15:00:00+03:00' or '2021-06-01T15:00:00+00:00'.")

class TrackingEventCodes(BaseModel):
    carrier: TrackingEventCodeDetail = Field(..., description="The original carrier specific tracking event codes and descriptions, i.e. the codes and descriptions provided by the carrier.")
    harmonised: Optional[TrackingEventCodeDetail] = Field(None, description="The harmonised tracking event codes and descriptions, i.e. if you are using translations in Gluey to translate between the carrier's codes and your own set of codes.")
    gluey: TrackingEventCodeDetail = Field(..., description="Glueys own tracking event codes and descriptions, i.e. the codes and descriptions that Gluey uses to harmonise between our and the carriers event codes.")
    gluey_milestone: Optional[str] = Field(None, description="The Gluey milestone classification of the tracking event, e.g., 'IN-TRANSIT', 'DEPARTED', 'ARRIVED', 'DELIVERED' etc.")

class TrackingEventPhysicalData(BaseModel):
    weight: Optional[Weight] = Field(None, description="The weight of the parcel at the time of the tracking event. Value in kg.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel at the time of the tracking event. All values in cm.")

class TrackingEventDeliveryConfirmation(BaseModel):
    """Class representing the delivery confirmation of the shipment / parcel."""
    signed_by: Optional[str] = Field(None, description="The name of the person who signed for the parcel.")
    base64_photo: Optional[str] = Field(None, description="The base64 encoded photo of the proof of the delivery.")
    photo_format: ImageFormat = Field(..., description="The format of the photo, e.g. 'JPEG', 'PNG' etc.")

class TrackingEvent(BaseModel):
    meta_data: Optional[list[MetaData]] = Field(None, description="Vary depending on carrier. All additional data from the tracking event that isn't part of the Gluey standard interface.")
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
    tracking_number: str = Field(..., description="The tracking number of the parcel")
    condition: ParcelCondition = Field(ParcelCondition.UNKNOWN, description="The current condition of the parcel as reported by the carrier.")
    carrier_weight_dims: Optional[TrackingEventPhysicalData] = Field(None, description="Physical data (i.e. weight and dimensions) of the parcel that the carrier have captured whilst processing the parcel in their facilities.")
    tracking_data: Optional[TrackingData] = Field(None, description="Available if tracking_level = 'parcel'. The tracking data for the individual parcel.")