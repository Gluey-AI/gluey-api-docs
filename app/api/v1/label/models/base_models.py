from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import BaseAddress, Contact, GeoLocation
from app.api.v1.common.utils import get_enum_description

class Incoterm(str, Enum):
    """Enum representing the Incoterms for international trade.
    
    Incoterms define the responsibilities of sellers and buyers
    for the delivery of goods under sales contracts. These terms
    standardize the process and clarify when the transfer of goods
    and costs occurs.
    """
    EXW = 'exw'
    FCA = 'fca'
    CPT = 'cpt'
    CIP = 'cip'
    DAP = 'dap'
    DPU = 'dpu'
    DDP = 'ddp'
    DDU = 'ddu'
    FAS = 'fas'
    FOB = 'fob'
    CFR = 'cfr'
    CIF = 'cif'

incoterm_descriptions = {
    Incoterm.EXW: "Ex Works: The seller makes the goods available at their premises. The buyer is responsible for all transportation costs and bears the risks for bringing the goods to their final destination.",
    Incoterm.FCA: "Free Carrier: The seller hands over the goods, cleared for export, to the carrier appointed by the buyer at the named place. The buyer bears all costs and risks from that point onwards.",
    Incoterm.CPT: "Carriage Paid To: The seller pays for the carriage of the goods to the named place of destination. The buyer assumes all risks after the goods have been delivered to the carrier.",
    Incoterm.CIP: "Carriage and Insurance Paid To: Similar to CPT, but the seller also contracts for insurance cover against the buyer’s risk of loss or damage to the goods during the carriage.",
    Incoterm.DAP: "Delivered at Place: The seller delivers the goods when they are placed at the disposal of the buyer on the arriving means of transport, ready for unloading at the named place of destination. The seller bears all risks involved in bringing the goods to the named place.",
    Incoterm.DPU: "Delivered at Place Unloaded: The seller delivers the goods when they are unloaded from the arriving means of transport and placed at the disposal of the buyer at the named place of destination. The seller bears all risks involved in bringing the goods to and unloading them at the named place.",
    Incoterm.DDP: "Delivered Duty Paid: The seller delivers the goods at the named place in the country of importation, paying all duties, taxes, and customs clearance costs. The buyer is responsible for unloading the goods at the destination.",
    Incoterm.DDU: "Delivered Duty Unpaid: The seller delivers the goods to the named place in the country of importation. The buyer is responsible for import duties, taxes, and customs clearance. The seller bears all risks and costs up to the named place of destination, excluding duties and taxes.",
    Incoterm.FAS: "Free Alongside Ship: The seller delivers when the goods are placed alongside the vessel at the named port of shipment. The buyer bears all costs and risks from that moment onwards.",
    Incoterm.FOB: "Free On Board: The seller delivers the goods on board the vessel nominated by the buyer at the named port of shipment. The buyer bears all costs and risks from that moment onwards.",
    Incoterm.CFR: "Cost and Freight: The seller pays for the cost and freight to bring the goods to the port of destination. Risk is transferred to the buyer once the goods are loaded on the vessel.",
    Incoterm.CIF: "Cost, Insurance, and Freight: Similar to CFR, but the seller also contracts for insurance cover against the buyer’s risk of loss or damage to the goods during the carriage."
}

class ExportReason(str, Enum):
    SALE = 'sale'
    RETURN_FOR_REFUND = 'return_for_refund'
    WARRANTY = 'warranty'
    REPAIR = 'repair'
    SAMPLE = 'sample'
    GIFT = 'gift'
    PERSONAL_EFFECTS = 'personal_effects'
    OTHER = 'other'

export_reason_descriptions = {
    ExportReason.SALE: "The goods are being exported for sale.",
    ExportReason.RETURN_FOR_REFUND: "The goods are being exported for a refund.",
    ExportReason.WARRANTY: "The goods are being exported for warranty purposes.",
    ExportReason.REPAIR: "The goods are being exported for repair.",
    ExportReason.SAMPLE: "The goods are being exported as a sample.",
    ExportReason.GIFT: "The goods are being exported as a gift.",
    ExportReason.PERSONAL_EFFECTS: "The goods are being exported as personal effects.",
    ExportReason.OTHER: "The goods are being exported for another reason."
}


class PackageType(str, Enum): 
    BOX = "box"
    ENVELOPE = "envelope"
    PADDED_ENVELOPE = "padded_envelope"
    JIFFY_BAG = "jiffy_bag"
    TUBE = "tube"
    FLAT_PACK = "flat_pack"
    CRATE = "crate"
    PALLET = "pallet"
    DRUM = "drum"
    COOLER_BOX = "cooler_box"
    RIGID_MAILER = "rigid_mailer"
    CUSTOM_PACKAGING = "custom_packaging"
    WINE_SHIPPER = "wine_shipper"
    FURNITURE_WRAP = "furniture_wrap"
    HAZMAT_CONTAINER = "hazmat_container"
    MEDICAL_TRANSPORT_CONTAINER = "medical_transport_container"
    RETURNABLE_PLASTIC_CONTAINERS = "returnable_plastic_containers"
    GUSSETED_BAG = "gusseted_bag"
    VACUUM_SEALED_BAG = "vacuum_sealed_bag"
    FOAM_LINED_BOX = "foam_lined_box"
    OTHER = "other"

package_type_descriptions = {
    PackageType.BOX: "A standard, versatile packaging option used for a variety of items. Typical for shoes, clothing, and electronics.",
    PackageType.ENVELOPE: "Used for documents and small flat items.",
    PackageType.PADDED_ENVELOPE: "An envelope with cushioning to protect delicate items. Also referred to as a 'bubble mailer'.",
    PackageType.JIFFY_BAG: "Lightweight, flexible plastic bag used for non-fragile items such as clothing. Also referred to as a 'poly mailer'.",
    PackageType.TUBE: "Cylindrical packaging used for posters, blueprints, and other long, thin items.",
    PackageType.FLAT_PACK: "Used for books, flat clothing, or other thin items.",
    PackageType.CRATE: "A heavy-duty wooden or plastic box used for large or heavy items.",
    PackageType.PALLET: "A platform used for transporting large quantities of items, often wrapped in plastic.",
    PackageType.DRUM: "Cylindrical container used for bulk liquids or granular items.",
    PackageType.COOLER_BOX: "Insulated box used for perishable or temperature-sensitive items.",
    PackageType.RIGID_MAILER: "A stiff, non-bendable envelope used for documents, photos, or artwork that needs protection from bending.",
    PackageType.CUSTOM_PACKAGING: "Tailored packaging solutions designed for specific products.",
    PackageType.WINE_SHIPPER: "Specialized packaging for shipping wine bottles safely.",
    PackageType.FURNITURE_WRAP: "Packaging materials like blankets and shrink wrap used for protecting furniture during transport.",
    PackageType.HAZMAT_CONTAINER: "Specially designed packaging for hazardous materials.",
    PackageType.MEDICAL_TRANSPORT_CONTAINER: "Specialized containers for transporting medical samples or pharmaceuticals.",
    PackageType.RETURNABLE_PLASTIC_CONTAINERS: "Reusable containers used for sustainable shipping solutions.",
    PackageType.GUSSETED_BAG: "A bag with expandable sides for bulkier items.",
    PackageType.VACUUM_SEALED_BAG: "Used for items that need to be kept airtight and protected from moisture.",
    PackageType.FOAM_LINED_BOX: "A box lined with foam for extra protection of fragile items.",
    PackageType.OTHER: "Any other type of packaging not listed above."
}


class Barcode(BaseModel):
    primary: str = Field(..., description="The primary barcode on the parcel. This is typically the carriers tracking id, but could also be another unique identifier for the parcel.")
    secondary: Optional[str] = Field(None, description="The secondary barcode on the parcel, if available.")

class DeliveryAddress(BaseAddress):
    name: str = Field(..., description="The name of the recipient such as an individual, company or organization")
    contact: Optional[Contact] = Field(None, description="The contact person at the address. Mandatory for collection requests.")
    suburb: Optional[str] = Field(None, description="The suburb or district. Only applicable to specific countries such as Australia and New Zealand.")
    what3words: Optional[str] = Field(None, description="The what3words address of the location. For example 'index.home.raft'")
    geo: Optional[GeoLocation] = Field(None, description="The geographical location of the address.")

class Addresses(BaseModel):
    from_address: DeliveryAddress = Field(None, description="Optional. Alternative address from where the shipment is from / collected / picked up.")
    to_address: DeliveryAddress = Field(..., description="The address of the to / recipient / receiver / consignee to where the shipment is delivered")
    undeliverable_address: Optional[DeliveryAddress] = Field(None, description="Optional. Alternative address to where the shipment / parcels that cannot be delivered are returned. Typically visible as the sender / return-to address on the label.")

class ManifestStatus(str, Enum):
    REQUIRED = 'required'
    OK = 'ok'
    PENDING_GLUEY = 'pending_gluey'

manifest_status_descriptions = {
    ManifestStatus.REQUIRED: "The carrier requires this shipment to be manifested and a separate call is needed to Gluey's manifesting / close-out endpoint.",
    ManifestStatus.OK: "The shipment has been successfully manifested / closed-out or does not require it.",
    ManifestStatus.PENDING_GLUEY: "The shipment is pending manifesting by Gluey."
}

class MethodOfShipment(str, Enum):
    AIR = 'air'
    SEA = 'sea'
    GROUND = 'ground'
    RAIL = 'rail'
    OTHER = 'other'

method_of_shipment_descriptions = {
    MethodOfShipment.AIR: "The shipment method is by air.",
    MethodOfShipment.SEA: "The shipment method is by sea.",
    MethodOfShipment.GROUND: "The shipment method is by ground.",
    MethodOfShipment.RAIL: "The shipment method is by rail.",
    MethodOfShipment.OTHER: "The shipment method is other than the specified options."
}

class QrCodeFormat(str, Enum):
    PNG = 'png'
    JPEG = 'jpeg'
    PDF = 'pdf'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'
    WEBP = 'webp'
    SVG = 'svg'

qr_code_format_descriptions = {
    QrCodeFormat.PNG: "PNG (Portable Network Graphics).",
    QrCodeFormat.JPEG: "JPEG (Joint Photographic Experts Group).",
    QrCodeFormat.PDF: "PDF (Portable Document Format).",
    QrCodeFormat.GIF: "GIF (Graphics Interchange Format).",
    QrCodeFormat.BMP: "BMP (Bitmap Image File).",
    QrCodeFormat.TIFF: "TIFF (Tagged Image File Format).",
    QrCodeFormat.WEBP: "WEBP (Web Picture format).",
    QrCodeFormat.SVG: "SVG (Scalable Vector Graphics)."
}

class LabelType(str, Enum):
    LABEL = 'label'
    QR_CODE = 'qr_code'
    PIN_CODE = 'pin_code'

label_type_descriptions = {
    LabelType.LABEL: "The label that is generated by Gluey / the carrier, typically in PDF, JPEG or ZPL format.",
    LabelType.QR_CODE: "The QR code that is generated by the carrier. Typically used for paperless returns.",
    LabelType.PIN_CODE: "The pin code for a parcel locker that the parcel is assigned to. Typically used for parcel lockers in convenience stores, gas stations etc.",
}

class LabelFormat(str, Enum):
    PDF = 'pdf'
    JPEG = 'jpeg'
    ZPL200 = 'zpl200'
    ZPL300 = 'zpl300'

label_format_descriptions = {
    LabelFormat.PDF: "Portable Document Format",
    LabelFormat.JPEG: "Joint Photographic Experts Group",
    LabelFormat.ZPL200: "Zebra Programming Language 200 dpi",
    LabelFormat.ZPL300: "Zebra Programming Language 300 dpi"
}

class LabelSize(str, Enum):
    """Enum representing the size of the label."""
    A4 = 'A4'
    _4x6 = '4x6'
    _4x7 = '4x7'
    _4x8 = '4x8'

label_size_descriptions = {
    LabelSize.A4: "A4 paper size",
    LabelSize._4x6: "4 inches (width) by 6 inches (height)",
    LabelSize._4x7: "4 inches (width) by 7 inches (height)",
    LabelSize._4x8: "4 inches (width) by 8 inches (height)"
}

class ParcelLockerPinCodeStatus(str, Enum):
    """Enum representing the status of the parcel locker pin code."""
    GENERATED = "generated"
    PENDING_CARRIER = "pending_carrier"

parcel_locker_pin_code_status_descriptions = {
    ParcelLockerPinCodeStatus.GENERATED: "The pin code has been generated and is ready to be used. The pin code is available in property 'pin_code' of the response.",
    ParcelLockerPinCodeStatus.PENDING_CARRIER: "The pin code is not yet ready and the carrier is still processing it. This pincode will have to be fetched via polling the 'Get Shipment' endpoint, or subscribing to the update shipment webhook"
}

class LabelRequest(BaseModel):
    """Class representing a label requested."""
    format: LabelFormat = Field(..., description=f"The format of the label that is requested. It can be one of the following:\n{get_enum_description(LabelFormat, label_format_descriptions)}")
    size: LabelSize = Field(..., description=f"The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services. It can be one of the following:\n{get_enum_description(LabelSize, label_size_descriptions)}")

class Label(BaseModel):
    """Class representing a generated label."""
    format: LabelFormat = Field(..., description=f"The format of the label that is requested. It can be one of the following:\n{get_enum_description(LabelFormat, label_format_descriptions)}")
    size: LabelSize = Field(..., description=f"The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services. It can be one of the following:\n{get_enum_description(LabelSize, label_size_descriptions)}")
    base64_label: str = Field(..., description="The label in base64 encoding.")

class CommercialInvoice(BaseModel):
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
    format: LabelFormat = Field(..., description=f"The format of the label that is requested. It can be one of the following:\n{get_enum_description(LabelFormat, label_format_descriptions)}")
    size: LabelSize = Field(..., description=f"The size of the label. If unspecified it defaults to '4x6' for Outbound carrier services, and 'A4' for return carrier services. It can be one of the following:\n{get_enum_description(LabelSize, label_size_descriptions)}")
    base64_encoded: str = Field(..., description="The base64 encoded label in the requested format and size.")

class QrCodeBaseModel(BaseModel):
    """Class representing a QR code that was generated by Gluey / the carrier."""
    format: QrCodeFormat = Field(..., description=f"The format of the QR code that is requested. It can be one of the following:\n{get_enum_description(QrCodeFormat, qr_code_format_descriptions)}")
    instructions: Optional[str] = Field(None, description="Instructions on how to use the QR code, for example 'Scan the QR code with your phone' etc.")
    base64_encoded: str = Field(..., description="The base64 encoded QR code.")

class ParcelLockerAddress(BaseAddress):
    """Parcel locker address contains all properties relevant to a parcel locker and its location."""
    name: str = Field(..., description="The name of the location where the parcel locker is, e.g. '7-Eleven', 'Shell', 'Tesco' etc.")
    contact: Optional[Contact] = Field(None, description="The contact person where the parcel locker is located.")
    what3words: Optional[str] = Field(None, description="The what3words address of the location. For example 'index.home.raft'")
    geo: Optional[GeoLocation] = Field(None, description="The geographical location of the address.")

class ParcelLockerBaseModel(BaseModel):
    """Class representing a parcel locker, including pin code, that the shipment is assigned to."""
    pin_code: Optional[str] = Field(None, description="The pin code for the parcel locker. Only available if the status is 'generated'.")
    locker_number: Optional[str] = Field(None, description="If applicable, some carriers only require the pin code. The locker number of the parcel locker, for example '1234' or 'A12' etc.")
    instructions: Optional[str] = Field(None, description="Instructions on how to use the parcel locker, for example 'Enter the pin code and close the door' etc.")
    address: Optional[ParcelLockerAddress] = Field(None, description="The address of the parcel locker. This is typically the address of the parcel locker location, e.g. 'Tesco, 123 Main Street, Anytown, USA'")

class ParcelLockerResponseModel(ParcelLockerBaseModel):
    """Class representing a parcel locker, including pin code, that the shipment is assigned to and if the code has been generated yet or not."""
    status: ParcelLockerPinCodeStatus = Field(..., description=f"The status of the parcel locker pin code. It can be one of the following:\n{get_enum_description(ParcelLockerPinCodeStatus, parcel_locker_pin_code_status_descriptions)}")