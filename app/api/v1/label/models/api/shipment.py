from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.api.v1.common.models.base_models import Dimensions, MetaData, References, TrackingLevel, Value, Weight
from app.api.v1.label.models.base_models import Addresses, Barcode, ManifestStatus, PackageType
from app.api.v1.label.models.api.carrier import Carrier
from app.api.v1.label.models.api.customs_clearance import CustomsClearance

class Item(BaseModel):
    """Class representing an item included in each parcel."""
    id: str = Field(..., description="The unique identifier for the item.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")
    description: str = Field(..., description="A description of the item, e.g. 'Blue Printed T-shirt', 'Samsung Xperia 1 III' etc.")
    quantity: int = Field(..., description="The quantity of this particular item in the parcel. If there are 2 T-shirts, then the quantity is 2.")
    unit_value: Value = Field(..., description="The monetary value of a single item. If total value is $100 and quantity is 2, then the unit value is $50.00")
    unit_weight: Optional[Weight] = Field(..., description="The weight of a single item. If total weight is 3kg and quantity is 2, then the unit weight is 1.5kg.")
    hs_code: Optional[str] = Field(..., description="The Harmonized System (HS) code for the item. This is an internationally standardized system of names and numbers to classify traded products.")
    country_of_origin: Optional[str] = Field(..., description="The country where the item was produced or manufactured as a ISO 3166-1 alpha-2 ('US','GB','DE' etc) or alpha-3 ('USA', 'GBR', 'DEU') country code.")
    return_reason: Optional[str] = Field(None, description="The reason for the return of the item. This is typically a summary of the reason for the return, e.g. 'damaged', 'wrong size', 'changed my mind' etc.")
    sku: Optional[str] = Field(None, description="The Stock Keeping Unit (SKU) for the item. This is a unique identifier for the item in your inventory.")
    item_url: Optional[str] = Field(None, description="A URL to a webpage with more information about the item, e.g. a product page on the webshop.")

class Parcel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="The unique identifier for the parcel.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel. This will be included in subsequent messages such as tracking events, label responses etc.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags to assign to parcel. All meta data is included with subsequent tracking events. Maximum 20 key-value pairs.")
    tracking_number: str = Field(..., description="The tracking number of the parcel")
    barcodes: Barcode = Field(..., description="The barcodes visible on the parcel.")
    weight: Weight = Field(..., description="The total weight of the parcel. If left empty, Gluey will calculate the weight based on the items in the parcel.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel.")
    goods_description: Optional[str] = Field(None, description="A description of the goods in the parcel. This is typically a summary of the items in the parcel, e.g. 'electronics' or 'wearing appareal'.")
    package_type: Optional[PackageType] = Field(None, description="The type of package, e.g. 'box', 'envelope', 'pallet' etc.")
    items: Optional[list[Item]] = Field(None, description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class Shipment(BaseModel):
    """Class representing a shipment containing multiple parcels."""
    id: str = Field(..., description="The unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment. This will be included in subsequent messages such as tracking events and can be used to identify the shipment in your own system.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags to assign to shipment. All meta data is included with subsequent tracking events. Maximum 20 key-value pairs.")
    tracking_level: TrackingLevel = Field(..., description="The tracking level of the shipment. This indicates if the shipment is tracked at parcel level, shipment level. For shipments with multiple parcels, the parcels are only individually trackable when tracking-level is 'parcel'.")
    manifest_status: ManifestStatus = Field(..., description="The manifest status of the shipment. This indicates if the shipment needs to be manifested with carrier, if Gluey is handling it in the background, if it is not needed, or if it has been done.")
    manifest_id: Optional[str] = Field(..., description="The Gluey manifest id related to the shipment, if applicable and shipment is manifested.")
    eta: Optional[datetime] = Field(None, description="The estimated time of arrival for the shipment as provided by the carrier.")
    tracking_number: Optional[str] = Field(..., description="The tracking number of the Shipment (if available and carrier does not allow parcel-level tracking).")
    carrier: Carrier = Field(..., description="The carrier and carrier service assigned to this shipment.")
    references: References = Field(..., description="References for the shipment.")
    addresses: Addresses = Field(..., description="The addresses for collection, delivery and undeliverables.")
    customs_clearance: Optional[CustomsClearance] = Field(None, description="Customs clearance details about the shipment. Only applicable to cross-border shipments.")
    parcels: List[Parcel] = Field([], description="A list of parcels included in the shipment")