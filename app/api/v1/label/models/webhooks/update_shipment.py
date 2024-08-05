from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from app.api.v1.common.models.base_manifest import ManifestBaseModel
from app.api.v1.common.models.base_models import MetaData, References, TrackingLevel, tracking_level_descriptions
from app.api.v1.common.utils import get_enum_description
from app.api.v1.label.models.base_models import Barcode, LabelResponseBaseModel, ParcelLockerBaseModel, QrCodeBaseModel
from app.api.v1.label.models.webhooks.base_models import UpdateType, update_type_descriptions

class CollectionBookingResponse(BaseModel):
    carrier_collection_id: Optional[str] = Field(None, description="The carriers own unique identifier of this collection request.")
    carrier_payment_url: Optional[str] = Field(None, description="If applicable and additional charges apply. The URL to the page where the collection can be paid.")
    carrier_mangement_url: Optional[str] = Field(None, description="If available. The URL to the page where the collection can be managed by the shipper.")
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Additional meta data provided by the carrier.")

class ParcelWithLabel(BaseModel):
    id: str = Field(..., description="The unique identifier for the parcel. If not provided, Gluey will generate a unique identifier.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the parcel. This will be included in subsequent messages such as tracking events, label responses etc.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Meta data tags you assigned when it was created in Gluey.")
    carrier_label_meta_data: Optional[list[MetaData]] = Field([], description="The carrier and / or label specific metadata for the parcel that the carrier provided in their API response. These are unique keys that might be useful as identifiers of the parcel, rates etc.")
    carrier_tracking_id: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. This is the carriers own tracking id for the parcel")
    carrier_tracking_url: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    barcodes: Barcode = Field(..., description="The barcodes visible on the parcel.")
    label: LabelResponseBaseModel = Field(..., description="The labels, qr codes and / or parcel locker pin codes that was generated by Gluey / the carrier.")

class UpdateData(BaseModel):
    labels: Optional[list[ParcelWithLabel]] = Field(None, description="If `update_type=labels` this property will contain a list of the parcels that were a part of the the shipment including the label, tracking number and barcodes.")
    manifest: Optional[ManifestBaseModel] = Field(None, description="If `update_type=manifest` this property will be true if the shipment has been manifested with the carrier.")
    locker_pin: Optional[ParcelLockerBaseModel] = Field(None, description="If `update_type=locker_pin` this property will contain the parcel locker pin code that was generated for the shipment incl the location.")
    qr_code: Optional[QrCodeBaseModel] = Field(None, description="If `update_type=qr_code` this property will contain the QR code that was generated for the shipment.")
    collection: Optional[CollectionBookingResponse] = Field(None, description="If `update_type=collection` this property will contain the collection data that was generated by the carrier for the shipment.")
    other: Optional[list[MetaData]] = Field(None, description="If `update_type=other` this property will contain any other data that was updated for the shipment.")

class UpdateShipmentEvent(BaseModel):
    id: str = Field(..., description="Glueys unique identifier for the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Shipment.")
    created_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was created in Gluey. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    updated_utc: datetime = Field(..., description="The date and time in Coordinated Universal Time (UTC+00:00) when the shipment was updated in Gluey. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+00:00'.")
    tracking_level: TrackingLevel = Field(..., description=f"Indicates if parcels can be individually trackable (i.e. the carrier support multi-parcel tracking) or if only the shipment itself can be tracked. It can be one of the following:\n{get_enum_description(TrackingLevel, tracking_level_descriptions)}")
    carrier_tracking_id: str = Field(..., description="This is the carriers own tracking id for the shipment.")
    carrier_tracking_url: str = Field(..., description="The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    meta_data: Optional[list[MetaData]] = Field(None, description="Meta data tags you assigned when it was created in Gluey.")
    references: References = Field(..., description="References for the shipment.")
    update_type: UpdateType = Field(..., description=f"The type of update that have been made to the shipment and which determine the type of data that will be included in the `update_data` property. It can be one of the following:\n{get_enum_description(UpdateType, update_type_descriptions)}")
    update_data: UpdateData = Field(..., description="The data related to the update.")