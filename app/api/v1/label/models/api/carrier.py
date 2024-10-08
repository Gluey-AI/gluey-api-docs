from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from app.api.v1.common.models.base_models import (
    Dimensions, MetaData, PaperlessLabelType,
    Volume, Weight, paperless_type_descriptions
)

from app.api.v1.common.utils import get_enum_description

class GlueyValueAddingServiceClass(str, Enum):
    SATURDAY_DELIVERY = "saturday_delivery"
    SUNDAY_DELIVERY = "sunday_delivery"
    HOLIDAY_DELIVERY = "holiday_delivery"
    TEMP_CONTROLLED_AMBIENT = "temp_controlled_ambient"
    TEMP_CONTROLLED_CHILLED = "temp_controlled_chilled"
    TEMP_CONTROLLED_FROZEN = "temp_controlled_frozen"
    TEMP_CONTROLLED_HEATED = "temp_controlled_heated"
    TEMP_CONTROLLED_DRY_ICE = "temp_controlled_dry_ice"
    TEMP_CONTROLLED_LIQUID_NITROGEN = "temp_controlled_liquid_nitrogen"
    TEMP_CONTROLLED_HUMIDITY = "temp_controlled_humidity"
    VERIFICATION_SIGNATURE = "verification_signature"
    VERIFICATION_AGE_CHECK = "verification_age_check"
    VERIFICATION_PROOF_OF_IDENTITY = "verification_proof_of_identity"
    DNG_HAZMAT = "dng_hazmat"
    PERISHABLE = "perishable"
    FRAGILE = "fragile"
    SHOCK_MONITORING = "shock_monitoring"
    INSURANCE = "insurance"
    CASH_ON_DELIVERY = "cash_on_delivery"
    ECO_DELIVERY = "eco_delivery"
    ELECTRIC_VEHICLE = "electric_vehicle"
    BIKE_COURIER = "bike_courier"
    MOTORBIKE_COURIER = "motorbike_courier"
    VEHICLE_WITH_LIFTGATE = "vehicle_with_tail_lift"
    TWO_MAN_LIFT = "two_man_lift"
    LONG_GOODS = "long_goods"
    OVERSIZED_GOODS = "oversized_goods"
    HEAVY_GOODS = "heavy_goods"
    PRE_NOTICE_CALL_RECEIVER = "pre_notice_call_receiver"
    PRE_NOTICE_EMAIL = "pre_notice_email"
    PRE_NOTICE_SMS = "pre_notice_sms"
    PRE_NOTICE_WHATSAPP = "pre_notice_whatsapp"
    PRE_NOTICE_WECHAT = "pre_notice_wechat"
    COLLECTION = "collection"
    COLLECTION_PREMIUM = "collection_premium"
    COLLECTION_TIME_WINDOW = "collection_time_window"
    COLLECTION_SAME_DAY = "collection_same_day"
    COLLECTION_FIXED_DAY = "collection_fixed_day"
    COLLECTION_AT_TERMINAL = "collection_at_terminal"
    COLLECTION_BULK = "collection_bulk"
    DELIVERY_PREMIUM = "delivery_premium"
    DELIVERY_TIME_WINDOW = "delivery_time_window"
    DELIVERY_TIMED = "delivery_timed"
    DELIVERY_SAME_DAY = "delivery_same_day"
    DELIVERY_NEXT_DAY = "delivery_next_day"
    DELIVERY_FIXED_DAY = "delivery_fixed_day"
    DELIVERY_WITH_ASSEMBLY = "delivery_with_assembly"
    DELIVERY_WITH_INSTALLATION = "delivery_with_installation"
    DELIVERY_WITH_DEBRIS_REMOVAL = "delivery_with_debris_removal"
    DELIVERY_WITH_APPLIANCE_SETUP = "delivery_with_appliance_setup"
    DELIVERY_ATTEMPT_LIMIT = "delivery_attempt_limit"
    DELIVERY_REDELIVERY_SERVICE = "delivery_redelivery_service"
    DELIVERY_TO_NEIGHBOR = "delivery_to_neighbor"
    DELIVERY_UNATTENDED = "delivery_unattended"
    DELIVERY_TO_LOCKER = "delivery_to_locker"
    DELIVERY_HOLD_AT_LOCATION = "delivery_hold_at_location"
    DELIVERY_DELAYED = "delivery_delayed"
    DELIVERY_CONTACTLESS = "delivery_contactless"
    DELIVERY_RURAL = "delivery_rural"
    DISPOSE_PACKAGING = "dispose_packaging"
    DISPOSE_OLD_ITEM = "dispose_old_item"
    CUSTOMS_DUTIES_AND_TAXES = "customs_duties_and_taxes"
    CUSTOMS_CLEARANCE = "customs_clearance"
    CUSTOMS_CLEARANCE_COMMERCIAL = "customs_clearance_commercial"
    PHOTO_CONFIRMATION = "photo_confirmation"
    SECURE = "secure"
    CONFIDENTIAL = "confidential"
    GOVERNMENT_CERTIFIED = "government_certified"
    OTHER = "other"

gluey_value_adding_service_class_descriptions = {
    GlueyValueAddingServiceClass.SATURDAY_DELIVERY: "The parcel is requested to be delivered on a Saturday if necessary, typical for B2C deliveries.",
    GlueyValueAddingServiceClass.SUNDAY_DELIVERY: "The parcel is requested to be delivered on a Sunday if necessary, typical for B2C deliveries.",
    GlueyValueAddingServiceClass.HOLIDAY_DELIVERY: "The parcel is requested to be delivered on a public holiday, typical for urgent deliveries.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_AMBIENT: "The parcel needs to be kept in a frost-free / ambient temperature during transport, typical for plants, flowers and even electronics.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_CHILLED: "The parcel needs a cold-chain and stay chilled during transport, typical for food, medicine etc.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_FROZEN: "The parcel needs a cold-chain and stay frozen during transport, typical for food, medicine etc.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_HEATED: "The parcel needs to be kept warm / heated during transport, typical for specific chemicals or sensitive electronics.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_DRY_ICE: "The parcel requires dry ice for cooling during transport.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_LIQUID_NITROGEN: "The parcel requires liquid nitrogen for freezing during transport.",
    GlueyValueAddingServiceClass.TEMP_CONTROLLED_HUMIDITY: "The parcel requires humidity control to prevent damage from moisture during transit.",
    GlueyValueAddingServiceClass.VERIFICATION_SIGNATURE: "The carrier needs to verify the receiver / consignee during delivery by getting a signature upon handing over the parcel, typical for high value goods etc.",
    GlueyValueAddingServiceClass.VERIFICATION_AGE_CHECK: "The carrier needs to verify the receiver / consignee during delivery by performing an age check / verification, typical for alcohol, tobacco with age restrictions.",
    GlueyValueAddingServiceClass.VERIFICATION_PROOF_OF_IDENTITY: "The carrier needs to verify the receiver / consignee during delivery by verifying that they are the named person on the parcel, typical for high value goods etc.",
    GlueyValueAddingServiceClass.DNG_HAZMAT: "The parcel contains dangerous goods (hazmat) and needs special handling, typical for chemicals, batteries etc.",
    GlueyValueAddingServiceClass.PERISHABLE: "The parcel contains perishable items and needs special handling, typical for food, flowers, plants etc.",
    GlueyValueAddingServiceClass.FRAGILE: "The parcel contains fragile items and needs special handling, typical for glass, ceramics, electronics, artworks etc.",
    GlueyValueAddingServiceClass.SHOCK_MONITORING: "The parcel requires monitoring for shocks and impacts during transit to prevent damage.",
    GlueyValueAddingServiceClass.INSURANCE: "The parcel content should be insured during transport, typical for high value goods etc.",
    GlueyValueAddingServiceClass.CASH_ON_DELIVERY: "The driver should collect a payment from the receiver / consignee during delivery.",
    GlueyValueAddingServiceClass.ECO_DELIVERY: "The carrier should deliver the parcel in an eco-friendly way, e.g. electric vehicle, electric bike or other low-carbon transport.",
    GlueyValueAddingServiceClass.BIKE_COURIER: "The parcel should be delivered using a bike courier for fast and eco-friendly delivery in urban areas.",
    GlueyValueAddingServiceClass.MOTORBIKE_COURIER: "The parcel should be delivered using a motorbike courier for fast delivery in congested areas.",
    GlueyValueAddingServiceClass.VEHICLE_WITH_LIFTGATE: "The delivery vehicle should be equipped with a tail lift / liftgate for easy loading and unloading of heavy parcels.",
    GlueyValueAddingServiceClass.TWO_MAN_LIFT: "The delivery requires two personnel to lift and handle the parcel safely.",
    GlueyValueAddingServiceClass.LONG_GOODS: "The parcel contains long goods, e.g. furniture, pipes, planks etc.",
    GlueyValueAddingServiceClass.OVERSIZED_GOODS: "The parcel is oversized and requires special handling, typical for large appliances, furniture etc.",
    GlueyValueAddingServiceClass.HEAVY_GOODS: "The parcel is heavy and requires special handling or equipment for delivery.",
    GlueyValueAddingServiceClass.PRE_NOTICE_CALL_RECEIVER: "The driver of the delivery vehicle should call the receiver / consignee before they arrive at the delivery address, typical for B2C deliveries where re-delivery is costly.",
    GlueyValueAddingServiceClass.PRE_NOTICE_EMAIL: "The carrier should send a pre-notice email to the receiver / consignee before the delivery.",
    GlueyValueAddingServiceClass.PRE_NOTICE_SMS: "The carrier should send a pre-notice SMS to the receiver / consignee before the delivery.",
    GlueyValueAddingServiceClass.PRE_NOTICE_WHATSAPP: "The carrier should send a pre-notice WhatsApp message to the receiver / consignee before the delivery.",
    GlueyValueAddingServiceClass.PRE_NOTICE_WECHAT: "The carrier should send a pre-notice WeChat message to the receiver / consignee before the delivery.",
    GlueyValueAddingServiceClass.COLLECTION: "The carrier should collect the parcel from the sender, typical for B2B deliveries.",
    GlueyValueAddingServiceClass.COLLECTION_PREMIUM: "The carrier offers a premium collection service, e.g. within 1 hour, 2 hours etc.",
    GlueyValueAddingServiceClass.COLLECTION_TIME_WINDOW: "The carrier should collect the parcel from the sender within a specific time window, e.g. 10:00 - 12:00.",
    GlueyValueAddingServiceClass.COLLECTION_SAME_DAY: "The carrier should collect the parcel from the sender on the same day as the order is placed, if placed before the carrier's cut-off time.",
    GlueyValueAddingServiceClass.COLLECTION_FIXED_DAY: "The carrier should collect the parcel from the sender on a specific day, e.g. Monday, Wednesday, and Friday or a specific date, e.g. 2021-12-24.",
    GlueyValueAddingServiceClass.COLLECTION_AT_TERMINAL: "The parcel / delivery can be collected at a distribution center / terminal / depot of the carrier.",
    GlueyValueAddingServiceClass.COLLECTION_BULK: "The carrier should collect multiple parcels in one go, typical for large volume senders.",
    GlueyValueAddingServiceClass.DELIVERY_PREMIUM: "The carrier offers a premium delivery service, e.g. within 1 hour, 2 hours etc.",
    GlueyValueAddingServiceClass.DELIVERY_TIME_WINDOW: "The carrier should deliver the parcel to the receiver within a specific time window, e.g. 10:00 - 12:00.",
    GlueyValueAddingServiceClass.DELIVERY_TIMED: "The parcel should be delivered at a specific time requested by the receiver, e.g. 10:00, 14:00 etc. Normally +- 15-30 minutes.",
    GlueyValueAddingServiceClass.DELIVERY_SAME_DAY: "The carrier should deliver the parcel to the receiver on the same day as the order is placed, if placed before the carrier's cut-off time.",
    GlueyValueAddingServiceClass.DELIVERY_FIXED_DAY: "The carrier should deliver the parcel to the receiver on a specific day, e.g. Monday, Wednesday, and Friday or a specific date, e.g. 2021-12-24.",
    GlueyValueAddingServiceClass.DELIVERY_WITH_ASSEMBLY: "The carrier should assemble the delivered item, typical for furniture, exercise equipment etc.",
    GlueyValueAddingServiceClass.DELIVERY_WITH_INSTALLATION: "The carrier should install the delivered item, typical for appliances, electronics etc.",
    GlueyValueAddingServiceClass.DELIVERY_WITH_DEBRIS_REMOVAL: "The carrier should remove any debris or old items during delivery, typical for appliance replacements.",
    GlueyValueAddingServiceClass.DELIVERY_WITH_APPLIANCE_SETUP: "The carrier should set up appliances during delivery, typical for kitchen or laundry appliances.",
    GlueyValueAddingServiceClass.DELIVERY_ATTEMPT_LIMIT: "The carrier should limit the number of delivery attempts, typical for secure or high-value deliveries.",
    GlueyValueAddingServiceClass.DELIVERY_REDELIVERY_SERVICE: "The carrier offers a service to redeliver the parcel if the first attempt is unsuccessful.",
    GlueyValueAddingServiceClass.DELIVERY_TO_NEIGHBOR: "The carrier can deliver the parcel to a neighbor if the receiver is not available.",
    GlueyValueAddingServiceClass.DELIVERY_UNATTENDED: "The parcel can be delivered without the receiver being present, left in a safe place designated by the receiver.",
    GlueyValueAddingServiceClass.DELIVERY_TO_LOCKER: "The carrier can deliver the parcel to a designated locker location for pickup.",
    GlueyValueAddingServiceClass.DELIVERY_HOLD_AT_LOCATION: "The parcel should be held at a specified location for pickup by the receiver.",
    GlueyValueAddingServiceClass.DELIVERY_DELAYED: "The parcel delivery should be delayed until a specific date or time.",
    GlueyValueAddingServiceClass.DELIVERY_CONTACTLESS: "The parcel will be delivered without direct contact with the receiver.",
    GlueyValueAddingServiceClass.DELIVERY_RURAL: "The parcel is being delivered to a rural area / post code and might require special handling or additional time.",
    GlueyValueAddingServiceClass.DISPOSE_PACKAGING: "After delivery, the carrier should dispose of the packaging material, e.g. cardboard, plastic, foam etc.",
    GlueyValueAddingServiceClass.DISPOSE_OLD_ITEM: "After delivery, the carrier should dispose of an old item being replaced, e.g. old appliance, furniture etc.",
    GlueyValueAddingServiceClass.CUSTOMS_DUTIES_AND_TAXES: "The carrier should manage duties and taxes for the parcel, typical for international deliveries.",
    GlueyValueAddingServiceClass.CUSTOMS_CLEARANCE: "The carrier should handle custom clearance for international deliveries.",
    GlueyValueAddingServiceClass.CUSTOMS_CLEARANCE_COMMERCIAL: "The carrier should specifically do a commercial customs clearance for international deliveries (i.e. B2B clearance). Typically means the carrier will required commercial invoices, certificates of origin etc.",
    GlueyValueAddingServiceClass.PHOTO_CONFIRMATION: "The carrier should take a photo of the delivered parcel as proof of delivery.",
    GlueyValueAddingServiceClass.SECURE: "The parcel contains items that needs secure handling such as passports, ID cards, keys, visas and other types of legal documents.",
    GlueyValueAddingServiceClass.CONFIDENTIAL: "The parcel contains confidential information and needs secure handling.",
    GlueyValueAddingServiceClass.GOVERNMENT_CERTIFIED: "The carrier personnel handling the parcel should be certified by the government for specific types of deliveries.",
    GlueyValueAddingServiceClass.OTHER: "Any other value added service not covered by the above classifications."
}

class DeliveryFeature(str, Enum):
    ADDITIONAL_INSURANCE = "additional_insurance"
    AGGREGATOR_SERVICE = "aggregator_service"
    BEFORE_NOON = "before_noon"
    CASH_ON_DELIVERY = "cash_on_delivery"
    COLLECTION = "collection"
    CUSTOMS_CLEARANCE = "customs_clearance"
    CUSTOMS_CLEARANCE_COMMERCIAL = "customs_clearance_commercial"
    CUSTOMS_DUTIES_AND_TAXES = "customs_duties_and_taxes"
    DANGEROUS_GOODS = "dangerous_goods"
    DISPOSE_PACKAGING = "dispose_packaging"
    ECO_DELIVERY = "eco_delivery"
    EXPRESS = "express"
    FRAGILE = "fragile"
    GOVERNMENT = "government"
    HIGH_VALUE = "high_value"
    ITEM_EXCHANGE = "item_exchange"
    MILITARY = "military"
    NEXT_DAY = "next_day"
    ONLY_DELIVERY_ADDRESS = "only_delivery_address"
    OUTBOUND = "outbound"
    PARCEL_LOCKER = "parcel_locker"
    PERISHABLE = "perishable"
    PHOTO_CONFIRMATION = "photo_confirmation"
    POSTAL = "postal"
    PROOF_OF_DELIVERY = "proof_of_delivery"
    PUDO_DROP_OFF = "pudo_drop_off"
    PUDO_PICKUP = "pudo_pickup"
    PUDO_PICKUP_DROP_OFF = "pudo_pickup_drop_off"
    PRIORITY = "priority"
    RETURNS = "returns"
    SAME_DAY = "same_day"
    SCHEDULED_SATURDAY_DELIVERY = "scheduled_saturday_delivery"
    SECURE = "secure"
    TEMP_CONTROLLED = "temp_controlled"
    TWENTY_FOUR_HOUR = "24_hour"
    FOURTY_EIGHT_HOUR = "48_hour"
    SEVENTY_TWO_HOUR = "72_hour"
    VERIFICATION = "verification"
    WEEKEND_DELIVERY = "weekend_delivery"

delivery_feature_descriptions = {
    DeliveryFeature.ADDITIONAL_INSURANCE: "The carrier service should offer additional insurance coverage.",
    DeliveryFeature.AGGREGATOR_SERVICE: "Only show carrier services that is an aggregator service, i.e. the carrier is an aggregator of multiple carriers where they sell their own service but use a third-party carrier to actually deliver the parcel.",
    DeliveryFeature.BEFORE_NOON: "Only show carrier services where delivery is before noon (12:00 PM midday).",
    DeliveryFeature.CASH_ON_DELIVERY: "Only show carrier services that offer cash on delivery payments.",
    DeliveryFeature.COLLECTION: "Only show carrier services that offer parcel collection from a specified location.",
    DeliveryFeature.CUSTOMS_CLEARANCE: "Only show carrier services that handle customs clearance for international deliveries.",
    DeliveryFeature.CUSTOMS_CLEARANCE_COMMERCIAL: "Only show carrier services that handle commercial customs clearance for international B2B deliveries.",
    DeliveryFeature.CUSTOMS_DUTIES_AND_TAXES: "Only show carrier services that manage customs duties and taxes for international deliveries.",
    DeliveryFeature.DANGEROUS_GOODS: "Only show carrier services that handle dangerous goods.",
    DeliveryFeature.DISPOSE_PACKAGING: "Only show carrier services that offer packaging disposal after delivery.",
    DeliveryFeature.ECO_DELIVERY: "Only show carrier services that offer eco-friendly delivery options.",
    DeliveryFeature.EXPRESS: "Only show carrier services that offer express delivery.",
    DeliveryFeature.FRAGILE: "Only show carrier services that handle fragile items.",
    DeliveryFeature.GOVERNMENT: "Only show carrier services that support deliveries to government entities or agencies.",
    DeliveryFeature.HIGH_VALUE: "Only show carrier services that securely handle high-value items.",
    DeliveryFeature.ITEM_EXCHANGE: "Only show carrier services that offer item exchange during delivery.",
    DeliveryFeature.MILITARY: "Only show carrier services that support deliveries to military locations or personnel.",
    DeliveryFeature.NEXT_DAY: "Only show carrier services that offer next-day delivery.",
    DeliveryFeature.ONLY_DELIVERY_ADDRESS: "Only show carrier services that restrict delivery to a specific address without any safe-drop, neighbor delivery etc.",
    DeliveryFeature.OUTBOUND: "Only show carrier services that handle outbound deliveries.",
    DeliveryFeature.PARCEL_LOCKER: "Only show carrier services that deliver to secure parcel lockers.",
    DeliveryFeature.PERISHABLE: "Only show carrier services that handle perishable items.",
    DeliveryFeature.PHOTO_CONFIRMATION: "Only show carrier services that provide photo confirmation as proof of delivery.",
    DeliveryFeature.POSTAL: "Only show carrier services that use postal delivery.",
    DeliveryFeature.PROOF_OF_DELIVERY: "Only show carrier services that provide proof of delivery, such as a signature or electronic confirmation.",
    DeliveryFeature.PUDO_DROP_OFF: "Only show carrier services that offer drop-off at Pick-Up/Drop-Off (PUDO) locations, typically for returns.",
    DeliveryFeature.PUDO_PICKUP: "Only show carrier services that offer pickup from Pick-Up/Drop-Off (PUDO) locations, typically for outbound.",
    DeliveryFeature.PUDO_PICKUP_DROP_OFF: "Only show carrier services that offer both pickup and drop-off at Pick-Up/Drop-Off (PUDO) locations.",
    DeliveryFeature.PRIORITY: "Only show carrier services that offer priority delivery.",
    DeliveryFeature.RETURNS: "Only show carrier services that offer return services.",
    DeliveryFeature.SAME_DAY: "Only show carrier services that offer same-day delivery.",
    DeliveryFeature.SCHEDULED_SATURDAY_DELIVERY: "Only show carrier services that offer scheduled Saturday delivery.",
    DeliveryFeature.SECURE: "Only show carrier services that offer secure delivery for sensitive items.",
    DeliveryFeature.TEMP_CONTROLLED: "Only show carrier services that offer temperature-controlled delivery.",
    DeliveryFeature.TWENTY_FOUR_HOUR: "Only show carrier services that deliver within 24 hours of dispatch.",
    DeliveryFeature.FOURTY_EIGHT_HOUR: "Only show carrier services that deliver within 48 hours of dispatch.",
    DeliveryFeature.SEVENTY_TWO_HOUR: "Only show carrier services that deliver within 72 hours of dispatch.",
    DeliveryFeature.VERIFICATION: "Only show carrier services that require receiver verification during delivery, e.g. signature, age check etc.",
    DeliveryFeature.WEEKEND_DELIVERY: "Only show carrier services that also offer delivery on weekends, i.e. Monday all through to Saturday / Sunday."
}

class Labeling(str, Enum):
    LABEL = 'label'
    PAPERLESS = 'paperless'

labeling_descriptions = {
    Labeling.LABEL: "The carrier requires a physical label to be printed and attached to the parcel.",
    Labeling.PAPERLESS: "The carrier service is paperless and does not require a physical label to be attached to the parcel."
}

class Region(str, Enum):
    DOMESTIC = 'domestic'
    INTERNATIONAL = 'international'

region_descriptions = {
    Region.DOMESTIC: "The region is domestic, i.e. the from and to address is within the same country.",
    Region.INTERNATIONAL: "The region is international, i.e. the from and to address is in different countries."
}

class Direction(str, Enum):
    OUTBOUND = 'outbound'
    RETURN = 'return'

direction_descriptions = {
    Direction.OUTBOUND: "The carrier service is of type outbound and used to move a parcel from the shipper to the receiver.",
    Direction.RETURN: "The carrier service is of type return and used to move a parcel from the receiver back to the shipper."
}

class CarrierServiceType(str, Enum):
    AGGREGATOR_SERVICE = 'aggregator_service'
    DELIVERY = 'delivery'
    COLLECTION = 'collection'
    PICKUP_DROPOFF_POINT = 'pickup_dropoff_point'
    PARCEL_LOCKER = 'parcel_locker'

carrier_service_type_descriptions = {
    CarrierServiceType.AGGREGATOR_SERVICE: "The carrier service is a carrier aggregator service, i.e. the carrier is an aggregator of multiple carriers. Typically they would sell your their own service and then use a third-party carrier to actually deliver the parcel.",    
    CarrierServiceType.DELIVERY: "The carrier service is a delivery service, i.e. the parcel is delivered to the receiver's address.",
    CarrierServiceType.COLLECTION: "The carrier service is a collection service, i.e. the parcel is collected from the sender's address.",
    CarrierServiceType.PICKUP_DROPOFF_POINT: "The carrier service is a pickup and dropoff point service, i.e. the parcel is dropped off at a designated location for the receiver to collect, or the receiver drops the parcel here.",
    CarrierServiceType.PARCEL_LOCKER: "The carrier service is a locker service, i.e. the parcel is delivered to a designated parcel locker for the receiver to collect."
}


class CarrierInstructions(BaseModel):
    """Class representing special instructions for the carrier.
    
    NOTES! Please note that not all carriers support using instructions, and many carriers have specific value added services for this purpose (e.g. 'Call recipient before delivery').
    Please check the Gluey documentation for the carrier and carrier service you are using.
    """
    delivery_instructions: Optional[str] = Field(None, description="The instruction for the carrier to take into account during the delivery, e.g. 'Leave at front door'.")
    goods_instructions: Optional[str] = Field(None, description="Handling instructions for the goods, e.g. 'The blue side up'.")
    recipient_instructions: Optional[str] = Field(None, description="Instructions for the recipient, e.g. 'Transfer to fridge immediately upon arrival'.")

class CarrierServiceRestrictions(BaseModel):
    max_weight: Optional[Weight] = Field(None, description="The weight restrictions for the parcels that can be shipped with this carrier service.")
    max_dims: Optional[Dimensions] = Field(None, description="The dimension restrictions for the parcels that can be shipped with this carrier service.")
    max_volume: Optional[Volume] = Field(None, description="The volume restrictions for the parcels that can be shipped with this carrier service.")
    max_pieces: Optional[int] = Field(None, description="The maximum number of pieces allowed for the carrier service, e.g. 5 for 5 pieces / parcels.")
    max_value: Optional[float] = Field(None, description="The maximum value allowed for the carrier service, e.g. 1000.0 for £1000.")
    max_value_currency: Optional[str] = Field(None, description="The currency of the maximum value allowed for the carrier service in ISO-Alpha 3 country code, e.g. `GBP` for British Pounds.")
    standard_insurance: Optional[float] = Field(None, description="The default / standard insurance value the carrier is covering with the carrier service, e.g. 100.0 for £100.")
    max_insurance: Optional[float] = Field(None, description="The maximum additional insurance excess that the carrier allows for the carrier service, e.g. 1000.0 for £1000.")
    insurance_currency: Optional[str] = Field(None, description="The currency of the standard / max insurance value the carrier is covering with the carrier service, e.g. `GBP` for British Pounds.")

class ValueAddedServiceData(BaseModel):
    """Class representing additional data that is required to use the value added service"""
    key: str = Field(..., description="The key / name of the additional data needed, e.g. 'insurance_excess_amount', 'insurance_excess_currency'.")
    data_type: str = Field(..., description="The data type of the additional data needed, e.g. 'float', 'string', 'integer' or 'enum'.")
    example: str = Field(..., description="An example of the additional data needed, e.g. '1000.0', 'GBP', '5', 'High quality goods'.")
    description: str = Field(..., description="A description of the type of additional data needed, e.g. for 'The monetary amount of additional insurance excess'.")
    can_hardcode: bool = Field(..., description="Flag indicating if the data can be hardcoded, meaning it is not the type of data that will vary from one shipment order to another.")

class ValueAddingService(BaseModel):
    id: str = Field(..., description="Glueys ID of the value adding service for a particular Carrier Service. This can typically be found in the library of carriers in Gluey is the carriers own ID of the value add, e.g. `signature`, `age_check`.")
    name: str = Field(..., description="The carriers own name of the value added service, e.g. `PreNotice SMS`, `Hazmat`, `Cash on Delivery`.")
    gluey_classification: GlueyValueAddingServiceClass = Field(..., description=f"Gluey's generalised classification of the value added service to enable comparison across carriers and carrier services. It can be one of the following:\n{get_enum_description(GlueyValueAddingServiceClass, gluey_value_adding_service_class_descriptions)}")
    additional_data: Optional[list[ValueAddedServiceData]] = Field(None, description="Any additional data that are need for this value-added service.")

class CarrierServiceBase(BaseModel):
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. `standard_ground`, `express`, `home_delivery`.")
    name: str = Field(..., description="The name of the carrier service, e.g. `Express`, `Standard`, `Economy`, `Parcel`.")
    features: list[DeliveryFeature] = Field(..., description=f"Additional features / capabilities the carrier service supports. It can be one of the following:\n{get_enum_description(DeliveryFeature, delivery_feature_descriptions)}")
    labeling: Labeling = Field(..., description=f"The type of labeling required for the carrier service. It can be one of the following:\n{get_enum_description(Labeling, labeling_descriptions)}")
    paperless_type: Optional[PaperlessLabelType] = Field(None, description=f"If `labeling=paperless` this is the type of paperless label the carrier service provide. It can be one of the following:\n{get_enum_description(PaperlessLabelType, paperless_type_descriptions)}")
    region: Region = Field(..., description=f"The region of the carrier service. It can be one of the following:\n{get_enum_description(Region, region_descriptions)}")
    restrictions: Optional[CarrierServiceRestrictions] = Field(None, description="The restrictions around weight, dimensions etc of parcels that can be allocated to the carrier service.")

class CarrierService(CarrierServiceBase):
    direction: Direction = Field(..., description=f"The type of service this is. It can be one of the following:\n{get_enum_description(Direction, direction_descriptions)}")
    service_type: CarrierServiceType = Field(..., description=f"The type of service this is. It can be one of the following:\n{get_enum_description(CarrierServiceType, carrier_service_type_descriptions)}")
    value_adding_services: Optional[list[ValueAddingService]] = Field([], description="Value adding services to use in conjunction with the main carrier service, i.e. for 'home_delivery' this might be things such as 'cash_on_delivery', 'verification_signature', 'insurance' etc.")

class Carrier(BaseModel):
    carrier_id: str = Field(..., description="Glueys ID that identifies the carrier in our system, e.g. `poste_italiane`, `yodel`. The Gluey ID of the carrier as found in the library of carriers in Gluey.")
    name: str = Field(..., description="The name of the carrier in a user-friendly, e.g. `FedEx`, `UPS`, `DPD`, `GLS`.")
    service: CarrierService = Field(..., description="The service you want to use for the carrier.")
    instructions: Optional[CarrierInstructions] = Field(None, description="Will be forwarded to carrier if they support it. Any special instructions for the carrier, e.g. 'Leave at front door', 'Blue side up'.")
    gluey_profile: Optional[str] = Field(None, description="If you maintain contract / account specific meta data for the carrier in Gluey, this is the reference to that configuration (e.g. 'GLY-12345678').")
