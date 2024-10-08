from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime

from app.api.v1.common.models.base_models import MetaData, TrackingLevel, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.base_models import Barcode, LabelResponseBaseModel, ManifestStatus, ParcelLockerResponseModel, QrCodeBaseModel, manifest_status_descriptions

class LabelCodesResponseModel(BaseModel):
    """The label, qr codes and / or parcel locker pin codes that was generated by Gluey / the carrier."""
    label: Optional[LabelResponseBaseModel] = Field(None, description="The label that was generated by Gluey / the carrier.")
    qr_code: Optional[QrCodeBaseModel] = Field(None, description="The QR code that was generated by the carrier, typically for a paperless return.")
    parcel_locker: Optional[ParcelLockerResponseModel] = Field(None, description="The parcel locker, including pin code, that the shipment is assigned to.")

class ItemResponseModel(BaseModel):
    """Class representing an item included in each parcel."""
    id: str = Field(..., description="The unique identifier for the item.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the item.")

class ParcelResponseModel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="Glueys own unique identifier for the parcel.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel.")
    carrier_tracking_id: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. This is the carriers own tracking id for the parcel")
    carrier_tracking_url: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    carrier_label_meta_data: Optional[list[MetaData]] = Field(None, description="The carrier and / or label specific metadata for the parcel that the carrier provided in their API response. These are unique keys that might be useful as identifiers of the parcel, rates etc.")
    barcodes: Barcode = Field(..., description="The barcodes that are visible on the parcel.")
    labels_codes: LabelCodesResponseModel = Field(..., description="The labels, qr codes and / or parcel locker pin codes that was generated by Gluey / the carrier.")
    label_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Meta data related to the label printed.")
    items: Optional[list[ItemResponseModel]] = Field([], description="A list of items (e.g. T-shirts, electronics etc) contained in the parcel. Optional, but required for customs clearance and cross-border commerce.")

class ShipmentResponseModel(BaseModel):
    """Class representing a shipment containing multiple parcels."""
    id: str = Field(..., description="The unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    updated_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was last updated in the Gluey system. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    manifest_status: ManifestStatus = Field(..., description=f"The manifest status of the shipment. It can be one of the following:\n{get_enum_description(ManifestStatus, manifest_status_descriptions)}")
    manifest_id: Optional[str] = Field(None, description="The Gluey manifest id related to the shipment, if applicable and shipment is manifested.")
    carrier_tracking_id: Optional[str] = Field(None, description="This is the carriers own tracking id for the shipment.")
    carrier_tracking_url: Optional[str] = Field(None, description="The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    carrier_collection_id: Optional[str] = Field(None, description="If a collection has been booked with the carrier. This is the carriers own collection id for the shipment.")
    eta: Optional[datetime] = Field(None, description="The estimated time of arrival for the shipment, if provided by the carrier.")
    parcels: list[ParcelResponseModel] = Field([], description="A list of parcels included in the shipment")