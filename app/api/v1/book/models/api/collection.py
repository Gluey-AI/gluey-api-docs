


from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Contact
from app.api.v1.common.utils import get_enum_description

class CarrierCollectionBase(BaseModel):
    time_id: str = Field(..., description="Glueys identifier of this particular collection date / time / time window.")
    cost: Optional[float] = Field(None, description="If available. If there is any additional cost associated with the collection for this particular date / time / time window.")
    cost_currency: Optional[str] = Field(None, description="If available. The currency (in ISO Alpha-3) of the cost associated with the collection for this particular date / time / time window, e.g. `USD`.")

class CarrierCollectionTimeWindow(CarrierCollectionBase):
    start: datetime = Field(..., description="The start date and time of the collection window. The datetime is in ISO 8601 format with time zone, e.g., `2024-07-12T09:00:00-04:00`.")
    end: datetime = Field(..., description="The end date and time of the collection window. The datetime is in ISO 8601 format with time zone, e.g., `2024-07-12T12:00:00-04:00`.")

class CarrierCollectionDateTime(CarrierCollectionBase):
    time: str = Field(..., description="The datetime in ISO 8601 format with time zone, e.g., `2024-07-12T09:00:00-04:00`")

class CarrierCollectionDate(CarrierCollectionBase):
    date: str = Field(..., description="The date in the format `YYYY-MM-DD`, e.g. `2022-01-01`")

class CarrierSuggestions(BaseModel):
    collection_dates: Optional[list[CarrierCollectionDate]] = Field(None, description="A list of dates when the shipment can be collected.")
    collection_datetimes: Optional[list[CarrierCollectionDateTime]] = Field(None, description="A list of dates with specific times when the shipment can be collected.")
    collection_time_windows: Optional[list[CarrierCollectionTimeWindow]] = Field(None, description="A list of dates with a time window for when the shipment can be collected for the suggested date.")

class CollectionStatus(str, Enum):
    PENDING = "pending"
    BOOKED = "booked"
    CANCELLED = "cancelled"
    FAILED = "failed"

collection_status_descriptions = {
    CollectionStatus.PENDING: "The collection request is pending.",
    CollectionStatus.BOOKED: "The collection request has been booked.",
    CollectionStatus.CANCELLED: "The collection request has been cancelled."
}

class CollectionResponse(BaseModel):
    collection_id: str = Field(..., description="Glueys unique identifier of the collection request.")
    collection_status: CollectionStatus = Field(..., description=f"The status of the collection request. It can be one of the following:\n{get_enum_description(CollectionStatus, collection_status_descriptions)}")
    uuid_ref: Optional[str] = Field(None, description="If provided. Your own unique identifier of the collection request.")
    carrier_collection_id: Optional[str] = Field(None, description="If available. The carriers unique identifier of this collection request.")
    carrier_suggestions: CarrierSuggestions = Field(..., description="A list of dates when the shipment can be collected. The dates are available in three different formats and which option you will get will depend on what the carrier supports:\n- `collection_dates` - the carrier only allows you to book a collection for a specific date, but without being able to specify what time, e.g. `2022-01-01`. \n- `collection_datetimes` - the carrier allows you to book a collection for a specific date and time, e.g. `2024-07-12T09:00:00-04:00`. \n- `collection_time_windows` - the carrier allows you to book a collection for a specific date, and they give you a time window during that date, e.g. `2024-07-12T09:00:00-04:00` to `2024-07-12T12:00:00-04:00`.")

class CollectionContact(BaseModel):
    name: str = Field(..., description="The name of the contact person at the address.")
    phone: str = Field(..., description="The phone number of the contact person at the address.")

class CollectionInfo(BaseModel):
    contact: CollectionContact = Field(..., description="The contact person at the address.")
    reference: Optional[str] = Field(None, description="Any reference from the consumer for the collection.")
    notes_to_carrier: Optional[str] = Field(None, description="Any notes you want to send to the carrier about the collection.")
    bring_label: Optional[bool] = Field(None, description="If supported. If you want the carrier to bring a label for the parcel. If not provided, the carrier will expect you to have the label printed and attached to the parcel already.")

class CollectionRequest(BaseModel):
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier of the collection request.")
    info: CollectionInfo = Field(..., description="Information about the collection.")
    collection_dates: list[str] = Field(..., description="A list of dates for when you want the shipment to be collected in the format `YYYY-MM-DD`, e.g. `2022-01-01`.")    

class BookingResponse(BaseModel):
    collection_status: CollectionStatus = Field(..., description=f"The status of the collection request. It can be one of the following:\n{get_enum_description(CollectionStatus, collection_status_descriptions)}")
    carrier_collection_id: Optional[str] = Field(None, description="If available. The carriers unique identifier of this collection request.")
    paymentUrl: Optional[str] = Field(None, description="If applicable and additional charges apply. The URL to the page where the collection can be paid.")