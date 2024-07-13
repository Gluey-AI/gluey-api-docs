from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.api.v1.common.models.base_models import Dimensions, MetaData, References, TrackingLevel, Value, Weight, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.api.dangerous_goods import ShipmentLevelDangerousGoods
from app.api.v1.label.models.base_models import Addresses, Barcode, CollectionTimeWindow, ManifestStatus, PackageType, manifest_status_descriptions
from app.api.v1.label.models.api.carrier import Carrier
from app.api.v1.label.models.api.customs_clearance import CustomsClearance

class Item(BaseModel):
    """Class representing an item included in each parcel."""
    id: str = Field(..., description="Glueys unique identifier for the item.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")
    description: str = Field(..., description="A description of the item, e.g. 'Blue Printed T-shirt', 'Samsung Xperia 1 III' etc.")
    quantity: int = Field(..., description="The quantity of this particular item in the parcel. If there are 2 T-shirts, then the quantity is 2.")
    unit_value: Value = Field(..., description="The monetary value of a single item. If total value is $100 and quantity is 2, then the unit value is $50.00")
    unit_weight: Optional[Weight] = Field(None, description="The weight of a single item. If total weight is 3kg and quantity is 2, then the unit weight is 1.5kg.")
    hs_code: Optional[str] = Field(None, description="The Harmonized System (HS) code for the item. This is an internationally standardized system of names and numbers to classify traded products.")
    country_of_origin: Optional[str] = Field(None, description="The country where the item was produced or manufactured as a ISO 3166-1 alpha-2 ('US','GB','DE' etc) or alpha-3 ('USA', 'GBR', 'DEU') country code.")
    return_reason: Optional[str] = Field(None, description="The reason for the return of the item. This is typically a summary of the reason for the return, e.g. 'damaged', 'wrong size', 'changed my mind' etc.")
    sku: Optional[str] = Field(None, description="The Stock Keeping Unit (SKU) for the item. This is a unique identifier for the item in your inventory.")
    item_url: Optional[str] = Field(None, description="A URL to a webpage with more information about the item, e.g. a product page on the webshop.")

class Parcel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="Glueys unique identifier for the parcel.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel. This will be included in subsequent messages such as tracking events, label responses etc.")
    meta_data_updates: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags you want to be included into any webhook update / tracking update we send to you. Maximum 20 key-value pairs.")
    carrier_tracking_id: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. This is the carriers own tracking id for the parcel")
    barcodes: Barcode = Field(..., description="The barcodes visible on the parcel.")
    weight: Weight = Field(..., description="The total weight of the parcel. If left empty, Gluey will calculate the weight based on the items in the parcel.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel.")
    goods_description: Optional[str] = Field(None, description="A description of the goods in the parcel. This is typically a summary of the items in the parcel, e.g. 'electronics' or 'wearing appareal'.")
    package_type: Optional[PackageType] = Field(None, description="The type of package, e.g. 'box', 'envelope', 'pallet' etc.")
    items: Optional[list[Item]] = Field(None, description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class Shipment(BaseModel):
    """Class representing a shipment containing multiple parcels."""
    id: str = Field(..., description="Glueys unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment. This will be included in subsequent messages such as tracking events and can be used to identify the shipment in your own system.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    meta_data_updates: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags you want to be included into any webhook update / tracking update we send to you. Maximum 20 key-value pairs.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    manifest_status: ManifestStatus = Field(..., description=f"The manifest status of the shipment. It can be one of the following:\n{get_enum_description(ManifestStatus, manifest_status_descriptions)}")
    manifest_id: Optional[str] = Field(None, description="The Gluey manifest id related to the shipment, if applicable and shipment is manifested.")
    eta: Optional[datetime] = Field(None, description="The estimated time of arrival for the shipment as provided by the carrier.")
    carrier_tracking_id: Optional[str] = Field(None, description="If `tracking_level=shipment`. This is the carriers own tracking id for the shipment, and it means that for multi-parcel shipments the parcels are not individually trackable.")
    carrier: Carrier = Field(..., description="The carrier and carrier service assigned to this shipment.")
    collection_times: Optional[list[CollectionTimeWindow]] = Field(None, description="A list of times when the shipment can be collected. How to use:\n- If you have a `specific collection time and date`, then provide a single collection time with only the `start` specified.\n- If you have a `single collection time window`, then provide a single collection time with both `start` and `end` specified.\n- If you have `multiple collection time windows` that are acceptable, and the carrier supports it, then provide multiple time windows where all have with both `start` and `end` specified.")
    dng_declaration: Optional[ShipmentLevelDangerousGoods] = Field(None, description="Optional. Shipment-level details are not mandatory for dangerous goods shipments, but `parcel-level` and `item-level` details are mandatory.")
    customs_clearance: Optional[CustomsClearance] = Field(None, description="Customs clearance details about the shipment. Only applicable to cross-border shipments.")
    references: References = Field(..., description="References for the shipment.")
    addresses: Addresses = Field(..., description="The addresses for collection, delivery and undeliverables.")
    parcels: List[Parcel] = Field([], description="A list of parcels included in the shipment")