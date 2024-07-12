from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.utils import get_enum_description

class TrackingLevel(str, Enum):
    SHIPMENT = "shipment"
    PARCEL = "parcel"

tracking_level_descriptions = {
    TrackingLevel.SHIPMENT: "The carrier only supports shipment-level tracking events, and hence parcels are not individually trackable (e.g. if one parcel gets lost-in-transit you will not know which one based on only the tracking events).",
    TrackingLevel.PARCEL: "The carrier supports parcel-level tracking events, and tracking will be available for each individual parcel."
}

class Value(BaseModel):
    """Class representing monetary value."""
    amount: float = Field(..., description="The monetary amount, e.g. 100.00, 200.50, 300.75 etc.")
    currency: str = Field(..., description="The currency code, e.g. 'USD', 'EUR', 'GBP' etc.")
    
class MetaData(BaseModel):
    """Class representing metadata tag."""
    key: str = Field(..., description="The key of the metadata, e.g. 'order_id', 'customer_id', 'user_name' etc.")
    value: str = Field(..., description="The value of the metadata, e.g. 'ORD123456', 'CUST123456' etc.")

class GeoLocation(BaseModel):
    """Class representing a geographical location."""
    lat: float = Field(..., description="The latitude of the location.")
    lng: float = Field(..., description="The longitude of the location.")

class Contact(BaseModel):
    """Class representing a contact person."""
    name: str = Field(..., description="The name of the contact person")
    email: Optional[str] = Field(None, description="The email address of the contact person")
    mobile: Optional[str] = Field(None, description="The mobile phone number of the contact person")

class BaseAddress(BaseModel):
    """Class representing an address."""
    street: str = Field(..., description="The first line of the address")
    street_2: Optional[str] = Field(None, description="The second line of the address")
    postal_code: Optional[str] = Field(None, description="The postal code or ZIP code. Mandatory for most countries except for a few countries in the middle east and africa.")
    city: str = Field(..., description="The city or town")
    state: Optional[str] = Field(None, description="The state or province. Only applicable to specific countries such as the US, Canada, Australia etc.")
    iso_country: str = Field(..., description="The ISO 3166-1 alpha-2 ('US','GB','DE' etc) or alpha-3 ('USA', 'GBR', 'DEU') country code")

class UnitOfWeight(str, Enum):
    KG = 'kg'
    LB = 'lb'
    G = 'g'
    OZ = 'oz'

unit_of_weight_descriptions = {
    UnitOfWeight.KG: "Kilogram unit of weight.",
    UnitOfWeight.LB: "Pound unit of weight.",
    UnitOfWeight.G: "Gram unit of weight.",
    UnitOfWeight.OZ: "Ounce unit of weight."
}

class UnitOfMeasurement(str, Enum):
    CM = 'cm'
    IN = 'in'
    M = 'm'
    FT = 'ft'
    MM = 'mm'
    YD = 'yd'

unit_of_measurement_descriptions = {
    UnitOfMeasurement.CM: "Centimeter unit of measurement.",
    UnitOfMeasurement.IN: "Inch unit of measurement.",
    UnitOfMeasurement.M: "Meter unit of measurement.",
    UnitOfMeasurement.FT: "Foot unit of measurement.",
    UnitOfMeasurement.MM: "Millimeter unit of measurement.",
    UnitOfMeasurement.YD: "Yard unit of measurement."
}

class Dimensions(BaseModel):
    """Class representing the dimensions of the parcel."""
    length: float = Field(..., description="The length of the parcel")
    width: float = Field(..., description="The width of the parcel")
    height: float = Field(..., description="The height of the parcel")
    unit: UnitOfMeasurement = Field(UnitOfMeasurement.CM, description="The unit of measurement for the dimensions. Default is 'cm' if left unspecified.")

class Weight(BaseModel):
    """Class representing weight."""
    value: float = Field(..., description="The weight, e.g. 1.5, 2.0, 3.5 etc.")
    unit: UnitOfWeight = Field(UnitOfWeight.KG, description="The unit of weight. Default is 'kg' if left unspecified.")

class DocumentFormat(str, Enum):
    PDF = 'pdf'
    JPEG = 'jpeg'
    PNG = 'png'
    DOCX = 'docx'
    XLSX = 'xlsx'
    XLS = 'xls'
    CSV = 'csv'
    OTHER = 'other'

document_format_descriptions = {
    DocumentFormat.PDF: "PDF (Portable Document Format).",
    DocumentFormat.JPEG: "JPEG (Joint Photographic Experts Group).",
    DocumentFormat.PNG: "PNG (Portable Network Graphics), often used for images requiring transparency.",
    DocumentFormat.DOCX: "DOCX, a Microsoft Word document format.",
    DocumentFormat.XLSX: "XLSX, a Microsoft Excel spreadsheet format.",
    DocumentFormat.XLS: "XLS, an older Microsoft Excel spreadsheet format.",
    DocumentFormat.CSV: "CSV (Comma-Separated Values)",
    DocumentFormat.OTHER: "Any other format not covered by the specified formats."
}

class DocumentSource(str, Enum):
    GLUEY = 'gluey'
    CARRIER = 'carrier'

document_source_descriptions = {
    DocumentSource.GLUEY: "The document is generated internally in Gluey's own systems.",
    DocumentSource.CARRIER: "The document is generated by the carrier."
}

class DocumentType(str, Enum):
    CARRIER_MANIFEST = 'carrier_manifest'
    COMMERCIAL_INVOICE = 'commercial_invoice'
    INVOICE = 'invoice'
    PROOF_OF_DELIVERY = 'proof_of_delivery'
    PICKUP_RECEIPT = 'pickup_receipt'
    LOAD_LIST = 'load_list'
    BOL = 'bol'
    WAYBILL = 'waybill'
    DANGEROUS_GOODS_PAPERWORK = 'dangerous_goods_paperwork'
    OTHER = 'other'

document_type_descriptions = {
    DocumentType.CARRIER_MANIFEST: "A carrier manifest is generated by the carrier when sending a manifest or close-out call. It lists all the parcels or shipments that are being sent out in a batch.",
    DocumentType.COMMERCIAL_INVOICE: "A commercial invoice is required for international trade and customs procedures. It includes details about the goods being shipped, such as the description, value, and country of origin.",
    DocumentType.INVOICE: "This is an invoice from the carrier to the sender or receiver, detailing the charges for the shipping services provided. It includes information about the shipment, cost breakdown, and payment terms.",
    DocumentType.PROOF_OF_DELIVERY: "A proof of delivery (POD) document is sent by the carrier to confirm that the parcel has been delivered to the recipient. It typically includes the recipient's signature, date, and time of delivery.",
    DocumentType.PICKUP_RECEIPT: "A pickup receipt is provided by the carrier when they pick up a parcel from the sender. It serves as an acknowledgment that the carrier has taken possession of the parcel and includes details such as the date, time, and location of the pickup.",
    DocumentType.LOAD_LIST: "A load list is generated by the carrier and includes all the parcels that are loaded onto a specific vehicle or container. It helps the carrier and the driver ensure that all parcels are accounted for during transport.",
    DocumentType.BOL: "A bill of lading (BOL) is a legal document issued by the carrier to the shipper. It serves as a receipt for the cargo and includes details about the type, quantity, and destination of the goods being shipped. It also serves as a contract between the carrier and the shipper.",
    DocumentType.WAYBILL: "A waybill is a document issued by the carrier that accompanies the shipment. It provides detailed information about the shipment, including the sender and recipient details, the route, and handling instructions.",
    DocumentType.DANGEROUS_GOODS_PAPERWORK: "Dangerous goods paperwork includes documentation required for the transportation of hazardous materials. It ensures compliance with regulations and includes information about the nature of the dangerous goods, handling instructions, and emergency procedures.",
    DocumentType.OTHER: "This category includes any other types of documents that are not covered by the specified categories. It allows for flexibility in case there are additional document types specific to certain carriers or situations."
}

class Document(BaseModel):
    """Class representing a document generated by either Gluey or the carrier."""
    format: DocumentFormat = Field(..., description=f"The format of the document that is requested. It can be one of the following:\n{get_enum_description(DocumentFormat, document_format_descriptions)}")
    type: DocumentType = Field(..., description=f"The type of document this is. It can be one of the following:\n{get_enum_description(DocumentType, document_type_descriptions)}")
    description: Optional[str] = Field(None, description="A description of the document, e.g. 'Commercial Invoice for customs'.")
    source: DocumentSource = Field(..., description=f"The source of the document and who generated it. It can be one of the following:\n{get_enum_description(DocumentSource, document_source_descriptions)}")
    base64_document: str = Field(..., description="The document in base64 encoding.")

class References(BaseModel):
    """Class representing references for the shipment."""
    shipper: Optional[str] = Field(None, description="The reference number that the shipper / sender / consignor use for this shipment, typically an order reference or similar.")
    receiver: Optional[str] = Field(None, description="The reference number that the receiver / recipient / consignee of this use shipment.")
    saas_provider: Optional[str] = Field(None, description="The reference number that the OMS / WMS / CMS etc as a third-party software provider use to identify this shipment.")

class GlueyPaidApiServices(BaseModel):
    """Gluey operations that come with a surcharge.
    """        
    address_correction: Optional[bool] = Field(None, description="If label call fails due to an address issue, Gluey will attempt to correct the address and retry the label call towards the carrier. Only one attempt will be made. If the address cannot be corrected, the label call will fail.")   
    smart_crop: Optional[bool] = Field(None, description="If either goods description (parcel.goods_description) or item description (item.description) is too long, Gluey will attempt to crop this description and retry the call.")

class GlueyFreeApiServices(BaseModel):
    """Gluey operations that can be used free of charge.
    """    
    auto_manifest: Optional[bool] = Field(None, description="If the carrier requires a manifest / close-out call, Gluey will automatically execute this in the background after the label can has finished.")
    dimension_conversion: Optional[bool] = Field(None, description="If the unit of dimensions of the parcel are not supported by the carrier, Gluey will convert the dimensions to a supported unit, e.g. from 'in' to 'cm'.")
    exchange_rate_conversion: Optional[bool] = Field(None, description="If the currency of any monetary value is not supported by the carrier, Gluey will convert the currency and monetary amount to the currency the carrier request. The system is configured to fetch exchange rates precisely at 00:00 (midnight) local time in the United Kingdom. Note that this corresponds to British Summer Time (BST) during daylight saving months and Greenwich Mean Time (GMT) otherwise.")    
    override_goods_descriptions: Optional[str] = Field(None, description="Hardcode the goods descriptions of the parcels by providing a string value here, e.g. 'electronics'. This will override any existing goods description.")
    override_weight: Optional[float] = Field(None, description="Hardcode the weight, by providing a float value here, e.g. '2.95'. This will be considered of unit 'kg' and will override the weight of the parcels.")
    weight_conversion: Optional[float] = Field(None, description="If the weight unit is not supported by the carrier, Gluey will convert the weight to a supported unit, e.g. from 'lb' to 'kg'.")    

class GlueyApiServices(BaseModel):
    """Gluey have many convenience services that can be triggered as part of the label call.
    
    Below are the various operations that can be executed as part of the label call.
    """
    free: Optional[GlueyFreeApiServices] = Field(None, description="Gluey operations that can be used free of charge.")
    paid: Optional[GlueyPaidApiServices] = Field(None, description="Gluey operations that come with a surcharge.")