
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Dimensions, GeoLocation, Weight

class ParcelCondition(str, Enum):
    """The condition of the parcel at the time of the tracking event."""
    GOOD = "good"
    """The parcel is in good condition."""
    DAMAGED = "damaged"
    """The parcel is damaged."""
    UNKNOWN = "unknown"
    """The condition of the parcel is unknown / not disclosed by carrier."""

class ImageFormat(str, Enum):
    """Enum representing the format of the image."""
    PNG = 'png'
    JPEG = 'jpeg'
    PDF = 'pdf'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'
    WEBP = 'webp'
    SVG = 'svg'

class LocationType(str, Enum):
    """Enum representing the type of location."""  
    AIRPORT = 'airport'
    """The location is an airport, typically a point of transit for air shipments."""
    
    POST_OFFICE = 'post_office'
    """The location is a post office where mail and parcels are handled."""
    
    PUDO = 'pudo'
    """The location is a pick up / drop-off point for customers, which could be a convenience store, grocery store etc."""
    
    WAREHOUSE = 'warehouse'
    """The location is a warehouse where goods are stored and managed."""
    
    DISTRIBUTION_CENTER = 'distribution_center'
    """The location is a distribution center where goods are distributed to various destinations."""
    
    CUSTOMS = 'customs'
    """The location is a customs facility where shipments are inspected and cleared for international transport."""
    
    SORTING_FACILITY = 'sorting_facility'
    """The location is a sorting facility where parcels are sorted by destination. Also referred to as 'carrier hub' sometimes. """
    
    LOCAL_DEPOT = 'local_depot'
    """The location is a local depot where parcels are temporarily held before delivery."""
    
    TRANSIT_CENTER = 'transit_center'
    """The location is a transit center where parcels are transferred between different modes of transport."""
    
    CUSTOMER_ADDRESS = 'customer_address'
    """The location is the customer's address, the final delivery destination."""
    
    RETURN_CENTER = 'return_center'
    """The location is a return center where returned goods are processed."""
    
    FREIGHT_TERMINAL = 'freight_terminal'
    """The location is a freight terminal where goods are transferred between different transportation modes, typically for larger shipments."""
    
    BORDER_CHECKPOINT = 'border_checkpoint'
    """The location is a border checkpoint where parcels are inspected and cleared for crossing international borders."""
    
    REGIONAL_HUB = 'regional_hub'
    """The location is a regional hub where parcels are consolidated and distributed within a region."""
    
    DELIVERY_TRUCK = 'delivery_truck'
    """The location is on a delivery truck, indicating the parcel is currently in transit."""
    
    PARCEL_LOCKER = 'parcel_locker'
    """The location is a parcel locker where parcels can be securely stored for customer pickup."""
    
    PORT = 'port'
    """The location is a seaport where goods are transferred to or from ships."""
    
    RAIL_TERMINAL = 'rail_terminal'
    """The location is a rail terminal where goods are transferred to or from trains."""
    
    OTHER = 'other'
    """The location is not covered by the other location types."""

class GlueyMilestone(str, Enum):
    """Enum representing the milestone types for Gluey."""
    START = 'start'
    """All events related to the start of the shipment / parcel journey."""

    COLLECTION = 'collection'
    """All collection events related to the shipment / parcel."""

    IN_TRANSIT = 'in_transit'
    """All in-transit events related to the shipment / parcel."""

    RETURN_CENTRE = 'return_centre'
    """All events related to the return center processing."""

    DELIVERY = 'delivery'
    """All delivery events related to the shipment / parcel."""

    POST_DELIVERY = 'post_delivery'
    """All post-delivery events related to the shipment / parcel."""

    EXCEPTION = 'exception'
    """All exception events related to the shipment / parcel."""

    OTHER = 'other'
    """All other events not covered by the other milestone types."""

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

class GlueyEventCodeDetail(BaseModel):
    milestone: GlueyMilestone = Field(..., description="The Gluey milestone classification of the tracking event, e.g., 'start', 'collection', 'return_centre' etc.")
    code: str = Field(..., description="The code of the tracking event, e.g. 'delivered'. See menu on the left-side under 'Tracking Event Codes' for all available codes.")
    sub_code: str = Field(..., description="The subcode of the tracking event, e.g. 'with_signature', 'left_with_neighbor'. See menu on the left-side under 'Tracking Event Codes' for all available codes.")
    freetext_detail: Optional[str] = Field(None, description="Additional detail in free text form about the tracking event provided by Gluey.")

class CarrierEventCodeDetail(BaseModel):
    code: str = Field(..., description="The code of the tracking event, e.g. 'DLV' for the carrier.")
    sub_code: Optional[str] = Field(None, description="The subcode of the tracking event, e.g. 'DEP-LHR', 'ARR-GTW', 'DLV-FD' etc.")
    freetext_detail: Optional[str] = Field(None, description="Additional detail in free text form about the tracking event provided by the carrier / Gluey.")

class HarmonisedEventCodeDetail(BaseModel):
    code: str = Field(..., description="The code of the tracking event, e.g. 'delivered' for Gluey or 'DLV' for the carrier.")
    sub_code: Optional[str] = Field(None, description="The subcode of the tracking event that you harmonised to.")
    freetext_detail: Optional[str] = Field(None, description="Additional detail in free text form about the tracking event provided by the carrier / Gluey.")

class TrackingEventDateTime(BaseModel):
    created_utc: str = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the tracking event was created in the Gluey system. The date and time of the tracking event is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    carrier_utc: str = Field(..., description="Local time for the carrier when the tracking event took place. The date and time of the tracking event is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00-05:00', '2021-06-01T15:00:00+03:00' or '2021-06-01T15:00:00+00:00'.")

class TrackingEventCodes(BaseModel):
    gluey: GlueyEventCodeDetail = Field(..., description="Glueys own tracking event codes and descriptions, i.e. the codes and descriptions that Gluey uses to harmonise between our and the carriers event codes.")
    carrier: CarrierEventCodeDetail = Field(..., description="The original carrier specific tracking event codes and descriptions, i.e. the codes and descriptions provided by the carrier.")
    harmonised: Optional[HarmonisedEventCodeDetail] = Field(None, description="The harmonised tracking event codes and descriptions, i.e. if you are using translations in Gluey to translate between the carrier's codes and your own set of codes.")

class TrackingEventDeliveryConfirmation(BaseModel):
    """Class representing the delivery confirmation of the shipment / parcel."""
    signed_by: Optional[str] = Field(None, description="The name of the person who signed for the parcel.")
    base64_photo: Optional[str] = Field(None, description="The base64 encoded photo of the proof of the delivery.")
    photo_format: ImageFormat = Field(..., description="The format of the photo, e.g. 'JPEG', 'PNG' etc.")

class TrackingEventPhysicalData(BaseModel):
    weight: Optional[Weight] = Field(None, description="The weight of the parcel at the time of the tracking event. Value in kg.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel at the time of the tracking event. All values in cm.")