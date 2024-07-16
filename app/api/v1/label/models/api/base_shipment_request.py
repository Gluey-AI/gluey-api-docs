from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import Dimensions, MetaData, References, Value, Weight
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.api.customs_clearance import CustomsClearance
from app.api.v1.label.models.api.dangerous_goods import ItemLevelDangerousGoods, ParcelLevelDangerousGoods, ShipmentLevelDangerousGoods
from app.api.v1.label.models.base_models import Addresses, PackageType, package_type_descriptions

class BaseItemRequestModel(BaseModel):
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")
    description: str = Field(..., description="A description of the item, e.g. 'Blue Printed T-shirt', 'Samsung Xperia 1 III' etc.")
    quantity: int = Field(..., description="The quantity of this particular item in the parcel. If there are 2 T-shirts, then the quantity is 2.")
    unit_value: Optional[Value] = Field(None, description="The monetary value of a single item. If total value is $100 and quantity is 2, then the unit value is $50.00")
    unit_weight: Optional[Weight] = Field(None, description="The weight of a single item. If total weight is 3kg and quantity is 2, then the unit weight is 1.5kg.")
    hs_code: Optional[str] = Field(None, description="The Harmonized System (HS) code for the item. This is an internationally standardized system of names and numbers to classify traded products.")
    country_of_origin: Optional[str] = Field(None, description="The country where the item was produced or manufactured as a ISO 3166-1 alpha-2 ('US','GB','DE' etc) or alpha-3 ('USA', 'GBR', 'DEU') country code.")
    return_reason: Optional[str] = Field(None, description="The reason for the return of the item. This is typically a summary of the reason for the return, e.g. 'damaged', 'wrong size', 'changed my mind' etc.")
    sku: Optional[str] = Field(None, description="The Stock Keeping Unit (SKU) for the item. This is a unique identifier for the item in your inventory.")
    image_urls: Optional[list[str]] = Field(None, description="A list of URLs to images of the item. This can be used to send return partners photos of the item.")
    item_url: Optional[str] = Field(None, description="A URL to a webpage with more information about the item, e.g. a product page on the webshop.")
    dng_declaration: Optional[ParcelLevelDangerousGoods] = Field(None, description="Details about dangerous goods in the parcel. Only applicable to dangerous goods shipments.")

class BaseParcelRequestModel(BaseModel):
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel. This will be included in subsequent messages such as tracking events, label responses etc.")
    meta_data_updates: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags you want to be included into any webhook update / tracking update we send to you. Maximum 20 key-value pairs.")
    weight: Weight = Field(..., description="The total weight of the parcel. Either parcel weight or item weight must be provided. If left empty and item weight provided, Gluey will calculate the weight based on the items in the parcel.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel.")
    goods_description: Optional[str] = Field(None, description="A description of the goods in the parcel. This is typically a summary of the items in the parcel, e.g. 'electronics' or 'wearing appareal'.")
    package_type: PackageType = Field(PackageType.OTHER, description=f"The type of package. It can be one of the following:\n{get_enum_description(PackageType, package_type_descriptions)}")
    dng_declaration: Optional[ParcelLevelDangerousGoods] = Field(None, description="Details about dangerous goods in the parcel. Only applicable to dangerous goods shipments.")
    items: Optional[list[BaseItemRequestModel]] = Field(None, description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class BaseShipmentRequestModel(BaseModel):
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment. This will be included in subsequent messages such as tracking events and can be used to identify the shipment in your own system.")
    meta_data_updates: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags you want to be included into any webhook update / tracking update we send to you. Maximum 20 key-value pairs.")
    dng_declaration: Optional[ShipmentLevelDangerousGoods] = Field(None, description="Optional. Shipment-level details are not mandatory for dangerous goods shipments, but `parcel-level` and `item-level` details are mandatory.")
    customs_clearance: Optional[CustomsClearance] = Field(None, description="Customs clearance details about the shipment. Only applicable to cross-border shipments.")
    references: References = Field(..., description="References for the shipment.")
    addresses: Addresses = Field(..., description="The addresses for collection, delivery and undeliverables.")
    parcels: list[BaseParcelRequestModel] = Field(..., description="A list of parcels included in the shipment")