from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class GlueyAdditionalServiceClass(str, Enum):
    """An internal Gluey classification assigned to each CarrierAdditionalService to classify the type and nature of the additional service."""

    SATURDAY_DELIVERY = "saturday_delivery"
    """The parcel is requested to be delivered on a Saturday if necessary, typical for B2C deliveries."""
    
    SUNDAY_DELIVERY = "sunday_delivery"
    """The parcel is requested to be delivered on a Sunday if necessary, typical for B2C deliveries."""

    HOLIDAY_DELIVERY = "holiday_delivery"
    """The parcel is requested to be delivered on a public holiday, typical for urgent deliveries."""

    TEMP_CONTROLLED_AMBIENT = "temp_controlled_ambient"
    """The parcel needs to be kept in a frost-free / ambient temperature during transport, typical for plants, flowers and even electronics."""

    TEMP_CONTROLLED_CHILLED = "temp_controlled_chilled"
    """The parcel needs a cold-chain and stay chilled during transport, typical for food, medicine etc"""

    TEMP_CONTROLLED_FROZEN = "temp_controlled_frozen"
    """The parcel needs a cold-chain and stay frozen during transport, typical for food, medicine etc."""

    TEMP_CONTROLLED_HEATED = "temp_controlled_heated"
    """The parcel needs to be kept warm / heated during transport, typical for specific chemicals or sensitive electronics."""
    
    TEMP_CONTROLLED_DRY_ICE = "temp_controlled_dry_ice"
    """The parcel requires dry ice for cooling during transport."""

    TEMP_CONTROLLED_LIQUID_NITROGEN = "temp_controlled_liquid_nitrogen"
    """The parcel requires liquid nitrogen for freezing during transport."""

    TEMP_CONTROLLED_HUMIDITY = "temp_controlled_humidity"
    """The parcel requires humidity control to prevent damage from moisture during transit."""

    VERIFICATION_SIGNATURE = "verification_signature"
    """The carrier needs to verify the receiver / consignee during delivery by getting a signature upon handing over the parcel, typical for high value goods etc."""

    VERIFICATION_AGE_CHECK = "verification_age_check"
    """The carrier needs to verify the receiver / consignee during delivery by performing an age check / verification, typical for alcohol, tobacco with age restrictions."""

    VERIFICATION_PROOF_OF_IDENTITY = "verification_proof_of_identity"
    """The carrier needs to verify the receiver / consignee during delivery by verifying that they are the named person on the parcel, typical for high value goods etc."""

    DNG_HAZMAT = "dng_hazmat"
    """The parcel containers dangerous goods (hazmat) and needs special handling, typical for chemicals, batteries etc."""

    PERISHABLE = "perishable"
    """The parcel contains perishable items and needs special handling, typical for food, flowers, plants etc"""

    FRAGILE = "fragile"
    """The parcel contains fragile items and needs special handling, typical for glass, ceramics, electronics, artworks etc."""

    SHOCK_MONITORING = "shock_monitoring"
    """The parcel requires monitoring for shocks and impacts during transit to prevent damage."""

    INSURANCE = "insurance"
    """The parcel content should be insured during transport, typical for high value goods etc."""

    CASH_ON_DELIVERY = "cash_on_delivery"
    """The driver should collect a payment from the receiver / consignee during delivery."""

    ECO_DELIVERY = "eco_delivery"
    """The carrier should deliver the parcel in an eco-friendly way, e.g. electric vehicle, electric bike or other low-carbon transport."""
    
    BIKE_COURIER = "bike_courier"
    """The parcel should be delivered using a bike courier for fast and eco-friendly delivery in urban areas."""

    MOTORBIKE_COURIER = "motorbike_courier"
    """The parcel should be delivered using a motorbike courier for fast delivery in congested areas."""

    VEHICLE_WITH_LIFTGATE = "vehicle_with_tail_lift"
    """The delivery vehicle should be equipped with a tail life / liftgate for easy loading and unloading of heavy parcels."""

    TWO_MAN_LIFT = "two_man_lift"
    """The delivery requires two personnel to lift and handle the parcel safely."""
    
    LONG_GOODS = "long_goods"
    """The parcel contains long goods, e.g. furniture, pipes, planks etc."""
    
    OVERSIZED_GOODS = "oversized_goods"
    """The parcel is oversized and requires special handling, typical for large appliances, furniture etc."""

    HEAVY_GOODS = "heavy_goods"
    """The parcel is heavy and requires special handling or equipment for delivery."""
    
    PRE_NOTICE_CALL_RECEIVER = "pre_notice_call_receiver"
    """The driver of the delivery vehicle should call the receiver / consignee before they arrive at the delivery address, typical for B2C deliveries where re-delivery is costly."""
    
    PRE_NOTICE_EMAIL = "pre_notice_email"
    """The carrier should send a pre-notice email to the receiver / consignee before the delivery."""
    
    PRE_NOTICE_SMS = "pre_notice_sms"
    """The carrier should send a pre-notice SMS to the receiver / consignee before the delivery."""
    
    PRE_NOTICE_WHATSAPP = "pre_notice_whatsapp"
    """The carrier should send a pre-notice WhatsApp message to the receiver / consignee before the delivery."""

    PRE_NOTICE_WECHAT = "pre_notice_whatsapp"
    """The carrier should send a pre-notice WeChat message to the receiver / consignee before the delivery."""

    COLLECTION = "collection"
    """The carrier should collect the parcel from the sender, typical for B2B deliveries."""
    
    COLLECTION_PREMIUM = "collection_premium"
    """The carrier offer a premium collection service, e.g. within 1 hour, 2 hours etc."""
    
    COLLECTION_TIME_WINDOW = "collection_time_window"
    """The carrier should collect the parcel from the sender within a specific time window, e.g. 10:00 - 12:00."""
    
    COLLECTION_SAME_DAY = "collection_same_day"
    """The carrier should collect the parcel from the sender on the same day as the order is placed, if placed before the carrier's cut-off time."""

    COLLECTION_FIXED_DAY = "collection_fixed_day"
    """The carrier should collect the parcel from the sender on a specific day, e.g. Monday, Wednesday and Friday or a specific date, e.g. 2021-12-24."""
    
    COLLECTION_AT_TERMINAL = "collection_at_terminal"
    """The parcel / delivery can be collected at a distribution center / terminal / depot of the carrier."""

    COLLECTION_BULK = "collection_bulk"
    """The carrier should collect multiple parcels in one go, typical for large volume senders."""

    DELIVERY_PREMIUM = "delivery_premium"
    """The carrier offer a premium delivery service, e.g. within 1 hour, 2 hours etc."""
    
    DELIVERY_TIME_WINDOW = "delivery_time_window"
    """The carrier should deliver the parcel to the receiver within a specific time window, e.g. 10:00 - 12:00."""

    DELIVERY_TIMED = "delivery_timed"
    """The parcel should be delivered at a specific time requested by the receiver, e.g. 10:00, 14:00 etc. Normally +- 15-30 minutes."""
    
    DELIVERY_SAME_DAY = "delivery_same_day"
    """The carrier should deliver the parcel to the receiver on the same day as the order is placed, if placed before the carrier's cut-off time."""

    DELIVERY_FIXED_DAY = "delivery_fixed_day"
    """The carrier should deliver the parcel to the receiver on a specific day, e.g. Monday, Wednesday and Friday or a specific date, e.g. 2021-12-24."""

    DELIVERY_WITH_ASSEMBLY = "delivery_with_assembly"
    """The carrier should assemble the delivered item, typical for furniture, exercise equipment etc."""

    DELIVERY_WITH_INSTALLATION = "delivery_with_installation"
    """The carrier should install the delivered item, typical for appliances, electronics etc."""

    DELIVERY_WITH_DEBRIS_REMOVAL = "delivery_with_debris_removal"
    """The carrier should remove any debris or old items during delivery, typical for appliance replacements."""

    DELIVERY_WITH_APPLIANCE_SETUP = "delivery_with_appliance_setup"
    """The carrier should set up appliances during delivery, typical for kitchen or laundry appliances."""

    DELIVERY_ATTEMPT_LIMIT = "delivery_attempt_limit"
    """The carrier should limit the number of delivery attempts, typical for secure or high-value deliveries."""

    DELIVERY_REDELIVERY_SERVICE = "delivery_redelivery_service"
    """The carrier offers a service to redeliver the parcel if the first attempt is unsuccessful."""

    DELIVERY_TO_NEIGHBOR = "delivery_to_neighbor"
    """The carrier can deliver the parcel to a neighbor if the receiver is not available."""

    DELIVERY_UNATTENDED = "delivery_unattended"
    """The parcel can be delivered without the receiver being present, left in a safe place designated by the receiver."""

    DELIVERY_TO_LOCKER = "delivery_to_locker"
    """The carrier can deliver the parcel to a designated locker location for pickup."""

    DELIVERY_HOLD_AT_LOCATION = "delivery_hold_at_location"
    """The parcel should be held at a specified location for pickup by the receiver."""

    DELIVERY_DELAYED = "delivery_delayed"
    """The parcel delivery should be delayed until a specific date or time."""

    DELIVERY_CONTACTLESS = "delivery_contactless"
    """The parcel will be delivered without direct contact with the receiver."""

    DELIVERY_RURAL = "delivery_rural"
    """The parcel is being delivered to a rural area / post code and might require special handling or additional time."""
    
    DISPOSE_PACKAGING = "dispose_packaging"
    """After delivery, the carrier should dispose of the packaging material, e.g. cardboard, plastic, foam etc."""
    
    DISPOSE_OLD_ITEM = "dispose_old_item"
    """After delivery, the carrier should dispose of an old item being replaced, e.g. old appliance, furniture etc."""

    CUSTOMS_DUTIES_AND_TAXES = "customs_duties_and_taxes"
    """The carrier should manage duties and taxes for the parcel, typical for international deliveries."""
    
    CUSTOM_CLEARANCE = "customs_clearance"
    """The carrier should handle custom clearance for international deliveries."""

    PHOTO_CONFIRMATION = "photo_confirmation"
    """The carrier should take a photo of the delivered parcel as proof of delivery."""

    SECURE = "secure"
    """The parcel contains items that needs secure handling such as passports, ID cards, keys, visas and other types of legal documents."""

    CONFIDENTIAL = "confidential"
    """The parcel contains confidential information and needs secure handling."""

    GOVERNMENT_CERTIFIED = "government_certified"
    """The carrier personnel handling the parcel should be certified by the government for specific types of deliveries."""

class Region(str, Enum):
    """Enum representing the region of the carrier service, i.e. domestic or international."""

    DOMESTIC = 'domestic'
    """The region is domestic, i.e. the from and to address is within the same country."""

    INTERNATIONAL = 'international'
    """The region is international, i.e. the from and to address is in different countries."""

class Direction(str, Enum):
    """Enum representing the direction of a carrier service, i.e. an outbound or return service."""

    OUTBOUND = 'outbound'
    """The carrier service is of type outbound and use to move a parcel from the shipper to the receiver."""

    RETURN = 'return'
    """The carrier service is of type return and use to move a parcel from the receiver back to the shipper."""

class CarrierServiceType(str, Enum):
    HOME_DELIVERY = 'home_delivery'
    """The carrier service is a home delivery service, i.e. the parcel is delivered to the receiver's home address."""

    COLLECTION_AT_HOME = 'collection_at_home'
    """The carrier service is a collection at home service, i.e. the parcel is collected from the sender's home address."""

    PICKUP_DROPOFF_POINT = 'pickup_dropoff_point'
    """The carrier service is a pickup and dropoff point service, i.e. the parcel is dropped off at a designated location for the receiver to collect, or the receiver drops the parcel here."""

    PARCEL_LOCKER = 'parcel_locker'
    """The carrier service is a locker service, i.e. the parcel is delivered to a designated parcel locker for the receiver to collect."""

class CarrierInstructions(BaseModel):
    """Class representing special instructions for the carrier.
    
    NOTES! Please note that not all carriers support using instructions, and many carriers have specific additional services for this purpose (e.g. 'Call recipient before delivery').
    Please check the Gluey documentation for the carrier and carrier service you are using.
    """
    delivery_instructions: str = Field(..., description="The instruction for the carrier to take into account during the delivery, e.g. 'Leave at front door'.")
    goods_instructions: str = Field(..., description="Handling instructions for the goods, e.g. 'The blue side up'.")
    recipient_instructions: str = Field(..., description="Instructions for the recipient, e.g. 'Transfer to fridge immediately upon arrival'.")

class AdditionalData(BaseModel):
    """Class representing additional data needed to use the ."""
    key: str = Field(..., description="The key of the additional data, e.g. 'account_number', 'customer_id', 'client_id'.")
    value: str = Field(..., description="The value of the additional data, e.g. 'GB12345678'.")

class CarrierServiceAdditionalService(BaseModel):
    name: str = Field(..., description="The carrier's own name of the additional service, e.g. 'PreNotice SMS', 'TimeWindow Pickup 13-16'")
    code: str = Field(..., description="The code representing the additional service provided by the carrier as found in the Gluey library of carriers, .e.g. '02', 'saturday_delivery' or 'RF'.")
    gluey_classification: GlueyAdditionalServiceClass = Field(..., description="Gluey's generalised classification of the additional service to enable comparison across carriers and carrier services, e.g. 'saturday_delivery', 'temp_controlled_ambient', 'verification_signature', 'insurance'.")
    additional_data: Optional[list[AdditionalData]] = Field(None, description="Any additional data used for this value-added service.")

class CarrierService(BaseModel):
    """Class representing a service provided by a parcel carrier."""
    name: str = Field(..., description="The name of the carrier service, e.g. 'Express', 'Standard', 'Economy', 'Parcel'.")
    code: str = Field(..., description="The code representing the service provided by the carrier as found in the Gluey library of carriers. For example 'express', 'standard', 'economy'.")
    direction: Direction = Field(..., description="The type of service this is, i.e. 'outbound', 'return' or 'unknown'")
    region: Region = Field(..., description="The region of the carrier service, i.e. 'domestic' or 'international'.")
    service_type: CarrierServiceType = Field(..., description="The type of service this is, e.g. 'home_delivery', 'collection_at_home', 'pickup_dropoff_point', 'parcel_locker'.")
    additional_services: Optional[CarrierServiceAdditionalService] = Field(None, description="Additional services to use in conjunction with the carrier service.")

class CustomCarrierProfileKey(BaseModel):
    """Class representing the customer's carrier profile keys that are identifiers of the customer in the carrier's system."""
    key: str = Field(..., description="The key / name of the customer specific carrier account key. For example 'account_number', 'customer_id', 'client_id' and similar. Typically mapped in the carrier's system to a specific customer account and included in the EDI / API request.")
    value: str = Field(..., description="The value of the customer specific carrier accunt key. For example the key is 'account_number' the value might be 'GB12345678'.")

class Carrier(BaseModel):
    """Class representing a parcel carrier implemented in Gluey."""
    name: str = Field(..., description="The name of the carrier in a user-friendly, e.g. 'FedEx', 'UPS', 'DPD', 'GLS'.")
    code: str = Field(..., description="The gluey code of the carrier as found in the library of carriers in Gluey. For example fedex, gls_logistics.")
    service: CarrierService = Field(..., description="The service you want to use for the carrier.")
    instructions: Optional[CarrierInstructions] = Field(None, description="Will be forwarded to carrier if they support it. Any special instructions for the carrier, e.g. 'Leave at front door', 'Blue side up'.")
    implementation_version: str = Field('v1', description="The version of the carrier implemented in Gluey, for example 'v1', 'v2'. Default is 'v1' if left unspecified.")
    gluey_carrier_profile_key: Optional[str] = Field(None, description="If you maintain contract / account specific keys for the carrier in Gluey, this is the reference to that configuration (e.g. 'GLY-12345678').")
