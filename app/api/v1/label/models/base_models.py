from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import BaseAddress, Contact, GeoLocation

class Incoterm(str, Enum):
    """Enum representing the Incoterms for international trade.
    
    Incoterms define the responsibilities of sellers and buyers
    for the delivery of goods under sales contracts. These terms
    standardize the process and clarify when the transfer of goods
    and costs occurs.
    """

    EXW = 'EXW'
    """Ex Works: The seller makes the goods available at their premises. The buyer is responsible for all transportation costs and bears the risks for bringing the goods to their final destination."""
    
    FCA = 'FCA'
    """Free Carrier: The seller hands over the goods, cleared for export, to the carrier appointed by the buyer at the named place. The buyer bears all costs and risks from that point onwards."""
    
    CPT = 'CPT'
    """Carriage Paid To: The seller pays for the carriage of the goods to the named place of destination. The buyer assumes all risks after the goods have been delivered to the carrier."""
    
    CIP = 'CIP'
    """Carriage and Insurance Paid To: Similar to CPT, but the seller also contracts for insurance cover against the buyer’s risk of loss or damage to the goods during the carriage."""
    
    DAP = 'DAP'
    """Delivered at Place: The seller delivers the goods when they are placed at the disposal of the buyer on the arriving means of transport, ready for unloading at the named place of destination. The seller bears all risks involved in bringing the goods to the named place."""
    
    DPU = 'DPU'
    """Delivered at Place Unloaded: The seller delivers the goods when they are unloaded from the arriving means of transport and placed at the disposal of the buyer at the named place of destination. The seller bears all risks involved in bringing the goods to and unloading them at the named place."""
    
    DDP = 'DDP'
    """Delivered Duty Paid: The seller delivers the goods at the named place in the country of importation, paying all duties, taxes, and customs clearance costs. The buyer is responsible for unloading the goods at the destination."""
    
    DDU = 'DDU'
    """Delivered Duty Unpaid: The seller delivers the goods to the named place in the country of importation. The buyer is responsible for import duties, taxes, and customs clearance. The seller bears all risks and costs up to the named place of destination, excluding duties and taxes. This term is less commonly used now as it has been replaced by DAP (Delivered at Place) in the latest Incoterms (Incoterms 2020)."""
    
    FAS = 'FAS'
    """Free Alongside Ship: The seller delivers when the goods are placed alongside the vessel at the named port of shipment. The buyer bears all costs and risks from that moment onwards."""
    
    FOB = 'FOB'
    """Free On Board: The seller delivers the goods on board the vessel nominated by the buyer at the named port of shipment. The buyer bears all costs and risks from that moment onwards."""
    
    CFR = 'CFR'
    """Cost and Freight: The seller pays for the cost and freight to bring the goods to the port of destination. Risk is transferred to the buyer once the goods are loaded on the vessel."""
    
    CIF = 'CIF'
    """Cost, Insurance, and Freight: Similar to CFR, but the seller also contracts for insurance cover against the buyer’s risk of loss or damage to the goods during the carriage."""

class ExportReason(str, Enum):
    """Enum representing the reason for exporting goods."""
    SALE = 'sale'
    """The goods are being exported for sale."""

    RETURN_FOR_REFUND = 'return_for_refund'
    """The goods are being exported for a refund."""

    WARRANTY = 'warranty'
    """The goods are being exported for warranty purposes."""

    REPAIR = 'repair'
    """The goods are being exported for repair."""

    SAMPLE = 'sample'
    """The goods are being exported as a sample."""

    GIFT = 'gift'
    """The goods are being exported as a gift."""

    PERSONAL_EFFECTS = 'personal_effects'
    """The goods are being exported as personal effects."""

    OTHER = 'other'
    """The goods are being exported for another reason."""

class PackageType(str, Enum):
    """The type of packaging the contents of the parcel is wrapped in"""
    
    BOX = "box"
    """A standard, versatile packaging option used for a variety of items. Typical for shoes, clothing, and electronics."""
    
    ENVELOPE = "envelope"
    """Used for documents and small flat items"""
    
    PADDED_ENVELOPE = "padded_envelope"
    """An envelope with cushioning to protect delicate items. Also referred to as a 'bubble mailer'."""
    
    JIFFY_BAG = "jiffy_bag"
    """Lightweight, flexible plastic bag used for non-fragile items such as clothing. Also referred to as a 'poly mailer'."""
    
    TUBE = "tube"
    """Cylindrical packaging used for posters, blueprints, and other long, thin items"""
    
    FLAT_PACK = "flat_pack"
    """Used for books, flat clothing, or other thin items"""
    
    CRATE = "crate"
    """A heavy-duty wooden or plastic box used for large or heavy items"""
    
    PALLET = "pallet"
    """A platform used for transporting large quantities of items, often wrapped in plastic"""
    
    DRUM = "drum"
    """Cylindrical container used for bulk liquids or granular items"""
    
    COOLER_BOX = "cooler_box"
    """Insulated box used for perishable or temperature-sensitive items"""
    
    RIGID_MAILER = "rigid_mailer"
    """A stiff, non-bendable envelope used for documents, photos, or artwork that needs protection from bending"""
    
    CUSTOM_PACKAGING = "custom_packaging"
    """Tailored packaging solutions designed for specific products"""
    
    WINE_SHIPPER = "wine_shipper"
    """Specialized packaging for shipping wine bottles safely"""
    
    FURNITURE_WRAP = "furniture_wrap"
    """Packaging materials like blankets and shrink wrap used for protecting furniture during transport"""
    
    HAZMAT_CONTAINER = "hazmat_container"
    """Specially designed packaging for hazardous materials"""
    
    MEDICAL_TRANSPORT_CONTAINER = "medical_transport_container"
    """Specialized containers for transporting medical samples or pharmaceuticals"""
    
    RETURNABLE_PLASTIC_CONTAINERS = "returnable_plastic_containers"
    """Reusable containers used for sustainable shipping solutions"""
    
    GUSSETED_BAG = "gusseted_bag"
    """A bag with expandable sides for bulkier items"""
    
    VACUUM_SEALED_BAG = "vacuum_sealed_bag"
    """Used for items that need to be kept airtight and protected from moisture"""
    
    FOAM_LINED_BOX = "foam_lined_box"
    """A box lined with foam for extra protection of fragile items"""

class Barcode(BaseModel):
    """Class representing the barcodes visible on the parcel."""
    primary: str = Field(..., description="The primary barcode value, typically the tracking number, or a unique identifier for the parcel.")
    secondary: Optional[str] = Field(None, description="The secondary barcode, if applicable.")

class DeliveryAddress(BaseAddress):
    """Delivery address contains all properties relevant to the operational delivery of a parcel."""
    name: str = Field(..., description="The name of the recipient such as an individual, company or organization")
    contact: Contact = Field(..., description="The contact person at the address.")
    suburb: Optional[str] = Field(..., description="The suburb or district. Only applicable to specific countries such as Australia and New Zealand.")
    what3words: Optional[str] = Field(None, description="The what3words address of the location. For example 'index.home.raft'")
    geo: Optional[GeoLocation] = Field(None, description="The geographical location of the address.")

class Addresses(BaseModel):
    """Class representing the addresses for the shipment."""
    shipper: DeliveryAddress = Field(..., description="The address of the from / sender / shipper / consignor. Also the address where to collect, and where to return undeliverable parcels unless alternative addresses are specified in 'undeliverable' and 'collection'.")
    receiver: DeliveryAddress = Field(..., description="The address of the to / recipient / receiver / consignee to where the shipment is delivered")
    collection: Optional[DeliveryAddress] = Field(None, description="Optional. Alternative address from where the shipment is from / collected / picked up.")
    undeliverable: Optional[DeliveryAddress] = Field(None, description="Optional. Alternative address to where the shipment / parcels that cannot be delivered are returned. Typically visible as the sender / return address on the label.")

class ManifestStatus(str, Enum):
    """Enum representing the status of the manifest."""
    NOT_REQUIRED = 'not_required'
    """The carrier has no separate endpoint / does not required manifesting of shipments."""

    REQUIRED = 'required'
    """The carrier requires this shipment to be manifested and a separate call is needed to Gluey's manifesting / close-out endpoint."""
    
    OK = 'ok'
    """The shipment has been successfully manifested / closed-out."""
    
    PENDING_GLUEY = 'pending_gluey'
    """The shipment is pending manifesting by Gluey."""

class MethodOfShipment(str, Enum):
    """The method of shipment."""
    AIR = 'air'
    SEA = 'sea'
    GROUND = 'ground'
    RAIL = 'rail'
    OTHER = 'other'

class QrCodeFormat(str, Enum):
    """Enum representing the format of the QR code."""
    PNG = 'png'
    JPEG = 'jpeg'
    PDF = 'pdf'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'
    WEBP = 'webp'
    SVG = 'svg'

class LabelFormat(str, Enum):
    """Enum representing the format of the label."""
    PDF = 'pdf'  # Portable Document Format
    JPEG = 'jpeg'  # Joint Photographic Experts Group
    ZPL200 = 'zpl200'  # Zebra Programming Language 200 dpi
    ZPL300 = 'zpl300'  # Zebra Programming Language 300 dpi

class LabelSize(str, Enum):
    """Enum representing the size of the label."""
    A4 = 'A4'
    """A4 paper size"""
    
    _4x6 = '4x6'
    """4 inches by 6 inches"""
    
    _4x7 = '4x7'
    """4 inches by 7 inches"""
    
    _4x8 = '4x8'
    """4 inches by 8 inches"""

class ParcelLockerPinCodeStatus(str, Enum):
    """Enum representing the status of the parcel locker pin code."""
    GENERATED = "generated"
    PENDING_CARRIER = "pending_carrier"

class LabelRequest(BaseModel):
    """Class representing a label requested."""
    format: LabelFormat = Field(..., description="The format of the label that is requested. For example 'PDF', 'JPEG', 'ZPL200' or 'ZPL300'")
    size: LabelSize = Field(..., description="The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services.")

class Label(BaseModel):
    """Class representing a generated label."""
    format: LabelFormat = Field(..., description="The format of the label that is requested. For example 'PDF', 'JPEG', 'ZPL200' or 'ZPL300'")
    size: LabelSize = Field(..., description="The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services.")
    base64_label: str = Field(..., description="The label in base64 encoding.")

class CommercialInvoice(BaseModel):
    """The details about the commercial invoice."""
    company_logo_base64: Optional[str] = Field(None, description="The company logo to use in base64 encoding. Should be square (256x256 ideally) and in PNG / JPG format.")
    method_of_shipment: MethodOfShipment = Field(MethodOfShipment.AIR, description="The method of shipment, e.g. 'air', 'sea' etc.")
    invoice_number: str = Field(..., description="The invoice number.")
    invoice_date: Optional[str] = Field(datetime.now().strftime("%Y-%m-%d"), description="The invoice date in ISO 8601 format, e.g. '2022-01-01'. Will default to the current date if left unspecified.")
    invoice_value: float = Field(..., description="The invoice value.")
    payment_terms: str = Field(..., description="The payment terms, .e.g. 'Net 30 days'.")
    freight_charges: float = Field(..., description="The freight charges related to the shipment.")
    freight_charges_currency: str = Field(..., description="The currency code related to freight charges, e.g. 'USD'.")
    insurance_charges: float = Field(..., description="The insurance charges related to the shipment.")
    insurance_charges_currency: str = Field(..., description="The currency code related to insurance charges, e.g. 'USD'.")

class LabelResponseBaseModel(BaseModel):
    """Class representing the label that was generated by Gluey / the carrier."""
    format: LabelFormat = Field(..., description="The format of the label that is requested. For example 'PDF', 'JPEG', 'ZPL200' or 'ZPL300'")
    size: LabelSize = Field(..., description="The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services.")
    base64_encoded: str = Field(..., description="The base64 encoded label in the requested format and size.")

class QrCodeBaseModel(BaseModel):
    """Class representing a QR code that was generated by Gluey / the carrier."""
    format: QrCodeFormat = Field(..., description="The format of the QR code that is requested. For example 'PDF', 'JPEG', 'PNG' etc.")
    instructions: Optional[str] = Field(None, description="Instructions on how to use the QR code, for example 'Scan the QR code with your phone' etc.")
    base64_encoded: str = Field(..., description="The base64 encoded QR code.")

class ParcelLockerAddress(BaseAddress):
    """Parcel locker address contains all properties relevant to a parcel locker and its location."""
    name: str = Field(..., description="The name of the location where the parcel locker is, e.g. '7-Eleven', 'Shell', 'Tesco' etc.")
    contact: Optional[Contact] = Field(..., description="The contact person where the parcel locker is located.")
    what3words: Optional[str] = Field(None, description="The what3words address of the location. For example 'index.home.raft'")
    geo: Optional[GeoLocation] = Field(None, description="The geographical location of the address.")

class ParcelLockerBaseModel(BaseModel):
    """Class representing a parcel locker, including pin code, that the shipment is assigned to."""
    pin_code: Optional[str] = Field(None, description="The pin code for the parcel locker. Only available if the status is 'generated'.")
    locker_number: Optional[str] = Field(..., description="If applicable, some carriers only require the pin code. The locker number of the parcel locker, for example '1234' or 'A12' etc.")
    instructions: Optional[str] = Field(None, description="Instructions on how to use the parcel locker, for example 'Enter the pin code and close the door' etc.")
    address: Optional[ParcelLockerAddress] = Field(..., description="The address of the parcel locker. This is typically the address of the parcel locker location, e.g. 'Tesco, 123 Main Street, Anytown, USA'")

class ParcelLockerResponseModel(ParcelLockerBaseModel):
    """Class representing a parcel locker, including pin code, that the shipment is assigned to and if the code has been generated yet or not."""
    status: ParcelLockerPinCodeStatus = Field(..., description="The status of the parcel locker pin code. If the status is 'generated', the pin code is ready to be used and provided below in property 'pin_code'. If the status is 'pending_carrier', the pin code is not yet ready and the carrier is still processing it. This pincode will have to be fetched via polling the 'Get Shipment' endpoint, or subscribing to the update shipment webhook.")