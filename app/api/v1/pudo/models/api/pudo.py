from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Dimensions, GeoLocation, MetaData
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.api.carrier import CarrierServiceBase

class PudoPointType(str, Enum):
    LOCKER = 'locker'
    STORE = 'store'
    POST_OFFICE = 'post_office'
    SERVICE_POINT = 'service_point'
    GAS_STATION = 'gas_station'
    CONVENIENCE_STORE = 'convenience_store'
    SUPERMARKET = 'supermarket'
    MALL = 'mall'
    LIBRARY = 'library'
    TRANSPORT_HUB = 'transport_hub'
    UNIVERSITY = 'university'
    BUSINESS_CENTER = 'business_center'
    GYM = 'gym'
    HOTEL = 'hotel'
    PARKING_GARAGE = 'parking_garage'
    AIRPORT = 'airport'
    TRAIN_STATION = 'train_station'
    COMMUNITY_CENTER = 'community_center'
    BANK = 'bank'
    SPORTS_VENUE = 'sports_venue'
    HOSPITAL = 'hospital'
    OTHER = 'other'

pudo_point_type_descriptions = {
    PudoPointType.LOCKER: "A secure locker where parcels can be picked up or dropped off.",
    PudoPointType.STORE: "A retail store that offers pick-up and drop-off services.",
    PudoPointType.POST_OFFICE: "A post office providing PUDO services.",
    PudoPointType.SERVICE_POINT: "A dedicated service point for parcel pick-up and drop-off.",
    PudoPointType.GAS_STATION: "A gas station offering PUDO services.",
    PudoPointType.CONVENIENCE_STORE: "A convenience store providing PUDO services.",
    PudoPointType.SUPERMARKET: "A supermarket with PUDO services.",
    PudoPointType.MALL: "A shopping mall offering PUDO services.",
    PudoPointType.LIBRARY: "A library providing PUDO services.",
    PudoPointType.TRANSPORT_HUB: "A transportation hub such as a train station or bus station offering PUDO services.",
    PudoPointType.UNIVERSITY: "A university campus providing PUDO services.",
    PudoPointType.BUSINESS_CENTER: "A business center offering PUDO services.",
    PudoPointType.GYM: "A gym offering PUDO services.",
    PudoPointType.HOTEL: "A hotel providing PUDO services.",
    PudoPointType.PARKING_GARAGE: "A parking garage with PUDO services.",
    PudoPointType.AIRPORT: "An airport offering PUDO services.",
    PudoPointType.TRAIN_STATION: "A train station providing PUDO services.",
    PudoPointType.COMMUNITY_CENTER: "A community center offering PUDO services.",
    PudoPointType.BANK: "A bank providing PUDO services.",
    PudoPointType.SPORTS_VENUE: "A sports venue offering PUDO services.",
    PudoPointType.HOSPITAL: "A hospital providing PUDO services.",
    PudoPointType.OTHER: "A PUDO point type that does not fit into the predefined categories."
}

class PudoPointStatus(str, Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    MAINTENANCE = 'maintenance'

pudo_point_status_descriptions = {
    PudoPointStatus.ACTIVE: "The PUDO point is active and available for use.",
    PudoPointStatus.INACTIVE: "The PUDO point is inactive and not available for use.",
    PudoPointStatus.MAINTENANCE: "The PUDO point is under maintenance."
}

class PaymentMethod(str, Enum):
    CASH = 'cash'
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    APPLE_PAY = 'apple_pay'
    GOOGLE_PAY = 'google_pay'
    SAMSUNG_PAY = 'samsung_pay'
    PAYPAL = 'paypal'
    ALIPAY = 'alipay'
    WECHAT_PAY = 'wechat_pay'
    PAYTM = 'paytm'
    MPESA = 'mpesa'
    BITCOIN = 'bitcoin'
    ETHEREUM = 'ethereum'
    SWISH = 'swish'

payment_method_descriptions = {
    PaymentMethod.CASH: "Physical currency payment.",
    PaymentMethod.CREDIT_CARD: "Payment using a credit card.",
    PaymentMethod.DEBIT_CARD: "Payment using a debit card.",
    PaymentMethod.APPLE_PAY: "Payment using Apple Pay.",
    PaymentMethod.GOOGLE_PAY: "Payment using Google Pay.",
    PaymentMethod.SAMSUNG_PAY: "Payment using Samsung Pay.",
    PaymentMethod.PAYPAL: "Payment using PayPal.",
    PaymentMethod.ALIPAY: "Payment using Alipay (China).",
    PaymentMethod.WECHAT_PAY: "Payment using WeChat Pay (China).",
    PaymentMethod.PAYTM: "Payment using Paytm (India).",
    PaymentMethod.MPESA: "Payment using M-Pesa (Kenya).",
    PaymentMethod.BITCOIN: "Payment using Bitcoin cryptocurrency.",
    PaymentMethod.ETHEREUM: "Payment using Ethereum cryptocurrency.",
    PaymentMethod.SWISH: "Payment using Swish (Sweden)."
}

class DayOfWeek(str, Enum):
    MON = 'mon'
    TUE = 'tue'
    WED = 'wed'
    THU = 'thu'
    FRI = 'fri'
    SAT = 'sat'
    SUN = 'sun'

day_of_week_descriptions = {
    DayOfWeek.MON: "Monday",
    DayOfWeek.TUE: "Tuesday",
    DayOfWeek.WED: "Wednesday",
    DayOfWeek.THU: "Thursday",
    DayOfWeek.FRI: "Friday",
    DayOfWeek.SAT: "Saturday",
    DayOfWeek.SUN: "Sunday"
}

class PudoAddress(BaseModel):
    name: str = Field(..., description="The name of the location")
    street: str = Field(..., description="The first line of the address")
    street_2: Optional[str] = Field(None, description="The second line of the address")
    postal_code: str = Field(..., description="The postal code or ZIP code")
    suburb: Optional[str] = Field(None, description="The suburb or district. Only applicable to specific countries such as Australia and New Zealand.")
    city: str = Field(..., description="The city or town")
    state: Optional[str] = Field(None, description="The state or province. Only applicable to specific countries such as the US, Canada, Australia etc.")
    iso_country: str = Field(..., description="The ISO 3166-1 alpha-2 ('US','GB','DE' etc) or alpha-3 ('USA', 'GBR', 'DEU') country code")

class ContactInformation(BaseModel):
    phone_number: Optional[str] = Field(None, description="The contact phone number for the PUDO point")
    email: Optional[str] = Field(None, description="The contact email address for the PUDO point")

class BusinessHours(BaseModel):
    day_of_week: DayOfWeek = Field(..., description="The day of the week, e.g., 'monday', 'tuesday'")
    open_time: Optional[str]= Field(None, description="The opening time, e.g., '09:00'. null if closed all day.")
    close_time: Optional[str] = Field(None, description="The closing time, e.g., '17:00'. null if closed all day.")

class PudoFacilities(BaseModel):
    car_parking: Optional[bool] = Field(None, description="Indicates if parking for a car is available at the PUDO point")
    bike_parking: Optional[bool] = Field(None, description="Availability of bike parking facilities")
    accessibility: Optional[bool] = Field(None, description="Indicates if the PUDO point is wheelchair accessible")
    waiting_area: Optional[bool] = Field(None, description="Indicates if there is a waiting area at the PUDO point")

class PudoCapacity(BaseModel):
    max_parcel_size: Optional[Dimensions] = Field(None, description="The maximum parcel size that can be handled at the PUDO point")
    max_parcel_weight: Optional[float] = Field(None, description="The maximum parcel weight that can be handled at the PUDO point in kg")
    capacity: Optional[int] = Field(None, description="The capacity of the PUDO point, e.g., number of lockers or storage space")

class PudoSecurity(BaseModel):
    cctv_surveillance: Optional[bool] = Field(None, description="Indicates if there is CCTV surveillance at the PUDO point")
    security_staff: Optional[bool] = Field(None, description="Indicates if there is security staff at the PUDO point")

class PudoTechnology(BaseModel):
    self_service_kiosk: Optional[bool] = Field(None, description="Indicates if there is a self-service kiosk at the PUDO point")
    wifi: Optional[bool] = Field(None, description="Indicates if WiFi is available for customers")
    power_backup: Optional[bool] = Field(None, description="Indicates if there is a power backup system")
    temperature_control: Optional[bool] = Field(None, description="Indicates if the PUDO point has temperature-controlled storage")

class PudoOperationalInfo(BaseModel):
    opening_date: Optional[str] = Field(None, description="The opening date of the PUDO point")
    manager_name: Optional[str] = Field(None, description="The name of the manager responsible for the PUDO point")
    emergency_contact: Optional[str] = Field(None, description="Emergency contact information for the PUDO point")
    time_zone: Optional[str] = Field(None, description="The time zone in which the PUDO point operates")
    public_holidays: Optional[list[str]] = Field(None, description="List of public holidays when the PUDO point is closed")
    temporary_closures: Optional[str] = Field(None, description="Information on any temporary closures or downtime, e.g., maintenance periods")

class PudoServiceFeatures(BaseModel):
    packaging_materials_available: Optional[bool] = Field(None, description="Indicates if packaging materials are available at the PUDO point")
    assistance_available: Optional[bool] = Field(None, description="Indicates if staff assistance is available at the PUDO point")

class PudoCustomerSupport(BaseModel):
    customer_support_hours: Optional[list[BusinessHours]] = Field(None, description="Hours during which customer support is available")
    language_support: Optional[list[str]] = Field(None, description="Languages supported at the PUDO point in ISO 639-1 format, e.g., 'en', 'fr', 'ar' etc.")
    online_chat_support: Optional[bool] = Field(None, description="Indicates if online chat support is available")  

class PudoUserExperience(BaseModel):
    queue_management_system: Optional[bool] = Field(None, description="Indicates if a queue management system is in place")
    average_wait_time: Optional[int] = Field(None, description="Average wait time for customers at the PUDO point, in minutes")
    customer_feedback: Optional[float] = Field(None, description="Customer feedback scores or ratings on a scale from 0 to 5")

class PudoFinTech(BaseModel):
    payment_methods_accepted: Optional[list[PaymentMethod]] = Field(None, description="List of accepted payment methods, e.g., cash, credit card, mobile payments")
    service_fees: Optional[str] = Field(None, description="Details on any service fees charged for PUDO services")
    atm_available: Optional[bool] = Field(None, description="Indicates if an ATM is available at the PUDO point")

class PudoEnvironmentalOptions(BaseModel):
    recycling_facilities: Optional[bool] = Field(None, description="Indicates if recycling facilities are available at the PUDO point")
    eco_friendly_packaging: Optional[bool] = Field(None, description="Indicates if eco-friendly packaging options are available")

class PudoPoint(BaseModel):
    id: str = Field(..., description="Glueys identifier for the PUDO point")
    carrier_location_id: str = Field(..., description="The carriers unique location identifier for the PUDO point")
    carrier_id: str = Field(..., description="The unique carrier identifier for the PUDO point")
    carrier_services: Optional[list[CarrierServiceBase]] = Field(None, description="Should the carrier have any restrictions on services available at the PUDO point, this is a list of the services that can be used at the PUDO point.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Vary depending on carrier. Additional data from pudo integration that isn't part of the Gluey standard interface.")
    name: str = Field(..., description="The name of the PUDO point")
    type: PudoPointType = Field(..., description=f"The type of PUDO point. It can be one of the following:\n{get_enum_description(PudoPointType, pudo_point_type_descriptions)}")
    status: PudoPointStatus = Field(..., description=f"The current status of the PUDO point. It can be one of the following:\n{get_enum_description(PudoPointStatus, pudo_point_status_descriptions)}")
    address: PudoAddress = Field(..., description="The address of the PUDO point")
    what3words: Optional[str] = Field(None, description="Optional - if provided by carrier. The what3words location of the PUDO point, e.g. 'index.home.raft'.")
    geo: Optional[GeoLocation] = Field(None, description="Optional - if provided by carrier. The geo location of the pudo point, e.g. '51.521251,-0.203586'.")
    contact_information: Optional[ContactInformation] = Field(None, description="The contact information for the PUDO point")
    business_hours: Optional[list[BusinessHours]] = Field(None, description="The business hours for the PUDO point")
    services_offered: Optional[list[str]] = Field(None, description="List of services offered at the PUDO point, e.g., 'Pick-Up', 'Drop-Off', 'Returns'")
    facilities: Optional[PudoFacilities] = Field(None, description="The facilities available at the PUDO point")
    capacity: Optional[PudoCapacity] = Field(None, description="The capacity of the PUDO point")
    security: Optional[PudoSecurity] = Field(None, description="The security features available at the PUDO point")
    technology: Optional[PudoTechnology] = Field(None, description="The technology available at the PUDO point")
    operational_info: Optional[PudoOperationalInfo] = Field(None, description="The operational information for the PUDO point")
    service_features: Optional[PudoServiceFeatures] = Field(None, description="The service features available at the PUDO point")
    customer_support: Optional[PudoCustomerSupport] = Field(None, description="The customer support features available at the PUDO point, such as hours of operation, language support etc.")
    user_experience: Optional[PudoUserExperience] = Field(None, description="The user experience features available at the PUDO point, such as queue management, wait times etc.")
    financial_options: Optional[PudoFinTech] = Field(None, description="The financial options available at the PUDO point")
    eco_options: Optional[PudoEnvironmentalOptions] = Field(None, description="The environmental options available at the PUDO point")