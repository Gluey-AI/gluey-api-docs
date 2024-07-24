from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.api.carrier import DeliveryFeature, delivery_feature_descriptions

class Restrictions(str, Enum):
    WEIGHT = "weight"
    DIMENSIONS = "dimensions"
    VOLUME = "volume"

restrictions_descriptions = {
    Restrictions.WEIGHT: "Any restriction that is based on the weight of the parcel.",
    Restrictions.DIMENSIONS: "Any restriction that is based on the dimensions of the parcel (height, length, width).",
    Restrictions.VOLUME: "Any restriction that is based on the volume of the parcel."
}

class CarrierTimeWindowBase(BaseModel):
    start: datetime = Field(..., description="The start date and time of the collection window. The datetime is in ISO 8601 format with time zone, e.g., `2024-07-12T09:00:00-04:00`.")
    end: datetime = Field(..., description="The end date and time of the collection window. The datetime is in ISO 8601 format with time zone, e.g., `2024-07-12T12:00:00-04:00`.")

class CarrierTimeWindow(CarrierTimeWindowBase):
    cost: Optional[float] = Field(None, description="If available. If there is any additional cost associated with the collection for this particular date / time / time window.")
    cost_currency: Optional[str] = Field(None, description="If available. The currency (in ISO Alpha-3) of the cost associated with the collection for this particular date / time / time window, e.g. `USD`.")

class CollectionStatus(str, Enum):
    PENDING = "pending"
    BOOKED = "booked"
    CANCELLED = "cancelled"

collection_status_descriptions = {
    CollectionStatus.PENDING: "The collection request is pending.",
    CollectionStatus.BOOKED: "The collection request has been booked.",
    CollectionStatus.CANCELLED: "The collection request has been cancelled."
}

class CarrierServiceCollectionDates(BaseModel):
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. `2CPR`, `2VPR`, `home_delivery`.")
    carrier_service_name: str = Field(..., description="The name of the carrier service, e.g. `Xpect Medium Return`, `Xpect Large Return`, `Home Delivery`")
    collection_time_windows: list[CarrierTimeWindow] = Field(..., description="A list of available collection time windows for the shipment.")

class CollectionRequest(BaseModel):
    carrier_service_id: Optional[str] = Field(None, description="Optional. If you want to limit the collection request to a specific carrier service, provide the carrier service id, e.g. `2CPR`.")
    collection_dates: Optional[list[str]] = Field(None, description="Optional. If not specified Gluey will return available time windows for five (5) days in advance. Provide a list of dates you wish to query for when you want the shipment to be collected. The dates must be in ISO 8601 format, e.g. `2024-07-12`.")
    skip_restrictions: Optional[list[Restrictions]] = Field(None, description=f"By default Gluey will check the carrier services against the data in the shipment (origin, destination, weight, dims and volume). These checks are based on the value provided by the carrier in terms of maximum weight and dims. If you wish to remove any of these checks, for example if you have a custom agreement about weight and dims for a service or you are happy to take a surcharge, you can set the feature flags here in order for Gluey to skip applying some restrictions.")
    features: Optional[list[DeliveryFeature]] = Field(None, description=f"A list of delivery features you can use to check if the carrier got a service that meet the required features.")

class CarrierServiceTransitTime(BaseModel):
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. `2CPR`, `2VPR`, `home_delivery`.")
    carrier_service_name: str = Field(..., description="The name of the carrier service, e.g. `Xpect Medium Return`, `Xpect Large Return`, `Home Delivery`")
    min_days: int = Field(..., description="Minimum estimated transit time in days")
    max_days: int = Field(..., description="Maximum estimated transit time in days")

class TransitTimeRequest(BaseModel):
    carrier_service_id: Optional[str] = Field(None, description="Optional. If you want to limit the transit time request to a specific carrier service, provide the carrier service id, e.g. `2CPR`.")

class ServiceAvailabilityRequest(BaseModel):
    skip_restrictions: Optional[list[Restrictions]] = Field(None, description=f"By default Gluey will check the carrier services against the data in the shipment (origin, destination, weight, dims and volume). These checks are based on the value provided by the carrier in terms of maximum weight and dims. If you wish to remove any of these checks, for example if you have a custom agreement about weight and dims for a service or you are happy to take a surcharge, you can set the feature flags here in order for Gluey to skip applying some restrictions. It can be one of the following:\n{get_enum_description(Restrictions, restrictions_descriptions)}")
    features: Optional[list[DeliveryFeature]] = Field(None, description=f"Set additional restrictions in checking for available services. For example if you are only interested in services that allows you to ship dangerous goods you can filter on this here. It can be one of the following:\n{get_enum_description(DeliveryFeature, delivery_feature_descriptions)}")

class CarrierServiceDeliveryDates(BaseModel):
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. `2CPR`, `2VPR`, `home_delivery`.")
    carrier_service_name: str = Field(..., description="The name of the carrier service, e.g. `Xpect Medium Return`, `Xpect Large Return`, `Home Delivery`")
    delivery_time_windows: list[CarrierTimeWindow] = Field(..., description="A list of available delivery time windows for the shipment.")

class DeliveryRequest(BaseModel):
    carrier_service_id: Optional[str] = Field(None, description="Optional. If you want to limit the delivery request to a specific carrier service, provide the carrier service id, e.g. `2CPR`.")
    delivery_dates: Optional[list[str]] = Field(None, description="Optional. If not specified Gluey will return available time windows for five (5) days in advance. Provide a list of dates you wish to query for when you want the shipment to be delivered. The dates must be in ISO 8601 format, e.g. `2024-07-12`.")