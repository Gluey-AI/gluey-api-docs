from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import MetaData
from app.api.v1.common.utils import get_enum_description

class DeliveryFeature(str, Enum):
    WEEKEND_HOLIDAY = "weekend_holiday"
    TEMP_CONTROLLED = "temp_controlled"
    VERIFICATION = "verification"
    DANGEROUS_GOODS = "dangerous_goods"
    PERISHABLE = "perishable"
    FRAGILE = "fragile"
    ADDITIONAL_INSURANCE = "additional_insurance"
    CASH_ON_DELIVERY = "cash_on_delivery"
    ECO_DELIVERY = "eco_delivery"
    ELECTRIC_VEHICLE = "electric_vehicle"
    BIKE_COURIER = "bike_courier"
    VEHICLE_WITH_LIFTGATE = "vehicle_with_liftgate"
    TWO_MAN_LIFT = "two_man_lift"
    OVERSIZED_GOODS = "oversized_goods"
    PRE_NOTICE = "pre_notice"
    COLLECTION = "collection"
    BRING_LABEL = "bring_label"
    PARCEL_LOCKER = "parcel_locker"
    DELIVERY_TIMED = "delivery_timed"
    DELIVERY_SAME_DAY = "delivery_same_day"
    DELIVERY_NEXT_DAY = "delivery_next_day"
    DELIVERY_FIXED_DAY = "delivery_fixed_day"
    DELIVERY_WITH_ASSEMBLY = "delivery_with_assembly"
    DELIVERY_WITH_INSTALLATION = "delivery_with_installation"
    DELIVERY_WITH_DEBRIS_REMOVAL = "delivery_with_debris_removal"
    DELIVERY_WITH_APPLIANCE_SETUP = "delivery_with_appliance_setup"
    DELIVERY_TO_NEIGHBOR = "delivery_to_neighbor"
    DELIVERY_UNATTENDED = "delivery_unattended"
    DELIVERY_CONTACTLESS = "delivery_contactless"
    DISPOSE_PACKAGING = "dispose_packaging"
    CUSTOMS_DUTIES_AND_TAXES = "customs_duties_and_taxes"
    CUSTOM_CLEARANCE = "custom_clearance"
    PHOTO_CONFIRMATION = "photo_confirmation"
    SECURE = "secure"

delivery_feature_descriptions = {
    DeliveryFeature.WEEKEND_HOLIDAY: "The parcel is requested to be delivered on a weekend or public holiday, typical for urgent deliveries.",
    DeliveryFeature.TEMP_CONTROLLED: "The parcel requires temperature control during transport, including options like ambient, chilled, frozen, heated, dry ice, liquid nitrogen, or humidity control.",
    DeliveryFeature.VERIFICATION: "The carrier needs to verify the receiver during delivery through methods such as signature, age check, or proof of identity.",
    DeliveryFeature.DANGEROUS_GOODS: "The parcel contains dangerous goods (hazmat) and requires special handling, typical for chemicals, batteries, etc.",
    DeliveryFeature.PERISHABLE: "The parcel contains perishable items and needs special handling, typical for food, flowers, plants, etc.",
    DeliveryFeature.FRAGILE: "The parcel contains fragile items and requires special handling, typical for glass, ceramics, electronics, artworks, etc.",
    DeliveryFeature.ADDITIONAL_INSURANCE: "The parcel content should be insured during transport, typical for high-value goods.",
    DeliveryFeature.CASH_ON_DELIVERY: "The driver should collect a payment from the receiver during delivery.",
    DeliveryFeature.ECO_DELIVERY: "The carrier should deliver the parcel in an eco-friendly way, e.g., electric vehicle, hydrogen vehicle, electric bike, or other low-carbon transport.",
    DeliveryFeature.ELECTRIC_VEHICLE: "The parcel should be delivered using an electric vehicle for eco-friendly delivery.",
    DeliveryFeature.BIKE_COURIER: "The parcel should be delivered using a bike courier for fast and eco-friendly delivery in urban areas.",
    DeliveryFeature.VEHICLE_WITH_LIFTGATE: "The delivery vehicle should be equipped with a tail lift/liftgate for easy loading and unloading of heavy parcels.",
    DeliveryFeature.TWO_MAN_LIFT: "The delivery requires two personnel to lift and handle the parcel safely.",
    DeliveryFeature.OVERSIZED_GOODS: "The parcel is oversized and requires special handling, typical for large appliances, furniture, etc.",
    DeliveryFeature.PRE_NOTICE: "The carrier should provide pre-notice to the receiver via call, email, SMS, WhatsApp, or WeChat before delivery.",
    DeliveryFeature.COLLECTION: "The carrier should collect the parcel from the sender, including options for premium collection, time window, same day, fixed day, at terminal, or bulk collection.",
    DeliveryFeature.BRING_LABEL: "The carrier should bring a label for the parcel during collection.",
    DeliveryFeature.PARCEL_LOCKER: "The carrier can deliver the parcel to a designated locker location for pickup.",
    DeliveryFeature.DELIVERY_TIMED: "The parcel should be delivered at a specific time requested by the receiver, typically within a +- 15-30 minutes window.",
    DeliveryFeature.DELIVERY_SAME_DAY: "The carrier should deliver the parcel to the receiver on the same day as the order is placed, if placed before the carrier's cut-off time.",
    DeliveryFeature.DELIVERY_NEXT_DAY: "The carrier should deliver the parcel to the receiver on the next day after the order is placed, if placed before the carrier's cut-off time.",
    DeliveryFeature.DELIVERY_FIXED_DAY: "The carrier should deliver the parcel to the receiver on a specific day, e.g., Monday, Wednesday, and Friday or a specific date.",
    DeliveryFeature.DELIVERY_WITH_ASSEMBLY: "The carrier should assemble the delivered item, typical for furniture, exercise equipment, etc.",
    DeliveryFeature.DELIVERY_WITH_INSTALLATION: "The carrier should install the delivered item, typical for appliances, electronics, etc.",
    DeliveryFeature.DELIVERY_WITH_DEBRIS_REMOVAL: "The carrier should remove any debris or old items during delivery, typical for appliance replacements.",
    DeliveryFeature.DELIVERY_WITH_APPLIANCE_SETUP: "The carrier should set up appliances during delivery, typical for kitchen or laundry appliances.",
    DeliveryFeature.DELIVERY_TO_NEIGHBOR: "The carrier can deliver the parcel to a neighbor if the receiver is not available.",
    DeliveryFeature.DELIVERY_UNATTENDED: "The parcel can be delivered without the receiver being present, left in a safe place designated by the receiver.",
    DeliveryFeature.DELIVERY_CONTACTLESS: "The parcel will be delivered without direct contact with the receiver.",
    DeliveryFeature.DISPOSE_PACKAGING: "After delivery, the carrier should dispose of the packaging material, e.g., cardboard, plastic, foam, etc.",
    DeliveryFeature.CUSTOMS_DUTIES_AND_TAXES: "The carrier should manage duties and taxes for the parcel, typical for international deliveries.",
    DeliveryFeature.CUSTOM_CLEARANCE: "The carrier should handle custom clearance for international deliveries.",
    DeliveryFeature.PHOTO_CONFIRMATION: "The carrier should take a photo of the delivered parcel as proof of delivery.",
    DeliveryFeature.SECURE: "The parcel contains items that need secure handling such as passports, ID cards, keys, visas, and other types of legal documents."
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

class ServiceAvailabilityRequest(BaseModel):
    features: Optional[list[DeliveryFeature]] = Field(None, description=f"A list of delivery features you can use to check if the carrier got a service that meet the required features. It can be one of the following:\n{get_enum_description(DeliveryFeature, delivery_feature_descriptions)}")

class BookingResponse(BaseModel):
    carrier_collection_id: Optional[str] = Field(None, description="If available. The carriers own unique identifier of this collection request.")
    carrier_payment_url: Optional[str] = Field(None, description="If applicable and additional charges apply. The URL to the page where the collection can be paid.")
    carrier_mangement_url: Optional[str] = Field(None, description="If available. The URL to the page where the collection can be managed by the shipper.")
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Additional meta data provided by the carrier.")

class BookingRequest(BaseModel):
    time_window: Optional[CarrierTimeWindowBase] = Field(None, description="Optional. If you wish to book a collection for the parcel, provide a valid time window. Query endpoint `/shipments/{id}/carrier/collection` to get available time windows, or check Glueys portal for values you can hardcode.")

class CarrierServiceDeliveryDates(BaseModel):
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. `2CPR`, `2VPR`, `home_delivery`.")
    carrier_service_name: str = Field(..., description="The name of the carrier service, e.g. `Xpect Medium Return`, `Xpect Large Return`, `Home Delivery`")
    delivery_time_windows: list[CarrierTimeWindow] = Field(..., description="A list of available delivery time windows for the shipment.")

class DeliveryRequest(BaseModel):
    carrier_service_id: Optional[str] = Field(None, description="Optional. If you want to limit the delivery request to a specific carrier service, provide the carrier service id, e.g. `2CPR`.")
    delivery_dates: Optional[list[str]] = Field(None, description="Optional. If not specified Gluey will return available time windows for five (5) days in advance. Provide a list of dates you wish to query for when you want the shipment to be delivered. The dates must be in ISO 8601 format, e.g. `2024-07-12`.")