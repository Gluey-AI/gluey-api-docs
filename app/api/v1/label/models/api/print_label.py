from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document, MetaData
from app.api.v1.label.models.api.base_shipment_response import BaseParcelResponseModel, BaseShipmentResponseModel
from app.api.v1.label.models.api.carrier_request import BaseCarrierServiceRequest
from app.api.v1.label.models.api.collection import CarrierTimeWindowBase
from app.api.v1.label.models.api.shipment_response import ShipmentResponseModel
from app.api.v1.label.models.base_models import Barcode, CommercialInvoice, DeliveryAddress, LabelRequest, LabelResponseBaseModel, ParcelLockerResponseModel, QrCodeBaseModel

class CollectionBookingResponse(BaseModel):
    carrier_collection_id: Optional[str] = Field(None, description="If available. The carriers own unique identifier of this collection request.")
    carrier_payment_url: Optional[str] = Field(None, description="If applicable and additional charges apply. The URL to the page where the collection can be paid.")
    carrier_mangement_url: Optional[str] = Field(None, description="If available. The URL to the page where the collection can be managed by the shipper.")
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Additional meta data provided by the carrier.")

class DeliveryBookingResponse(BaseModel):
    carrier_delivery_id: Optional[str] = Field(None, description="If available. The carriers own unique identifier of this delivery request.")
    carrier_payment_url: Optional[str] = Field(None, description="If applicable and additional charges apply. The URL to the page where the delivery can be paid.")
    carrier_mangement_url: Optional[str] = Field(None, description="If available. The URL to the page where the delivery can be managed by the receiver.")
    carrier_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Additional meta data provided by the carrier.")

class LabelCodesResponseModel(BaseModel):
    """The label, qr codes and / or parcel locker pin codes that was generated by Gluey / the carrier."""
    label: Optional[LabelResponseBaseModel] = Field(None, description="The label that was generated by Gluey / the carrier.")
    qr_code: Optional[QrCodeBaseModel] = Field(None, description="The QR code that was generated by the carrier, typically for a paperless return.")
    parcel_locker: Optional[ParcelLockerResponseModel] = Field(None, description="The parcel locker, including pin code, that the shipment is assigned to.")

class ParcelResponseModel(BaseParcelResponseModel):
    carrier_tracking_id: Optional[str] = Field(None, description="Only available when `tracking_level=parcel`. This is the carriers own tracking id for the parcel")
    carrier_tracking_url: Optional[str] = Field(None, description="If `tracking_level=shipment`. The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    barcodes: Barcode = Field(..., description="The barcodes that are visible on the parcel.")
    labels_codes: LabelCodesResponseModel = Field(..., description="The labels, qr codes and / or parcel locker pin codes that was generated by Gluey / the carrier.")
    label_meta_data: Optional[list[MetaData]] = Field(None, description="If available. Meta data related to the label printed.")

class ShipmentResponseModel(BaseShipmentResponseModel):
    carrier_tracking_id: Optional[str] = Field(None, description="If `tracking_level=shipment`. This is the carriers own tracking id for the shipment, and it means that for multi-parcel shipments the parcels are not individually trackable.")
    carrier_tracking_url: Optional[str] = Field(None, description="If `tracking_level=shipment`. The URL to the carriers tracking page for the shipment, e.g. 'https://carrier.com/track?tracking_id=1234567890'.")
    eta: Optional[datetime] = Field(None, description="The estimated time of arrival for the shipment, if provided by the carrier. The date and time of the shipment is in ISO 8601 format and includes the UTC-offset, e.g. '2021-06-01T12:00:00+01:00'.")
    parcels: list[ParcelResponseModel] = Field([], description="A list of parcels included in the shipment")

class PrintLabelSyncResponse(BaseModel):
    shipment: ShipmentResponseModel = Field(..., description="The shipment details, including the parcels, tracking numbers, barcodes and the labels.")
    documents: Optional[list[Document]] = Field([], description="Any documents that were requested by Gluey and / or returned from the carrier API.")
    delivery: Optional[DeliveryBookingResponse] = Field(None, description="The delivery details, including the carriers own unique identifier of the delivery, payment URL and management URL.")

class PrintAndBookSyncResponse(BaseModel):
    shipment: ShipmentResponseModel = Field(..., description="The shipment details, including the parcels, tracking numbers, barcodes and the labels.")
    collection: Optional[CollectionBookingResponse] = Field(None, description="The collection details, including the carriers own unique identifier of the collection, payment URL and management URL.")
    delivery: Optional[DeliveryBookingResponse] = Field(None, description="The delivery details, including the carriers own unique identifier of the delivery, payment URL and management URL.")
    documents: Optional[list[Document]] = Field([], description="Any documents that were requested by Gluey and / or returned from the carrier API.")

class AdditionalDocuments(BaseModel):
    commercial_invoice: Optional[CommercialInvoice] = Field(None, description="The details about the commercial invoice you wish Gluey to generate for the shipment.")

class PrintLabelRequest(BaseModel):
    carrier_service_id: BaseCarrierServiceRequest = Field(..., description="The carrier service ID that should be used to generate the label, e.g. `ups_express`.")
    book_delivery: Optional[CarrierTimeWindowBase] = Field(None, description="For delivery services. The specific delivery time window to book with the carrier. Query endpoint `/shipments/{id}/carrier/delivery` to get available time windows, or check Glueys portal for values you can hardcode.")
    label: Optional[LabelRequest] = Field(None, description="The label requested, including the size and type. Only applicable to services where a label is generated, for paperless services this is not required.")

class PrintAndBookRequest(BaseModel):
    carrier_service_id: BaseCarrierServiceRequest = Field(..., description="The carrier service ID that should be used to generate the label, e.g. `ups_express`.")
    book_delivery: Optional[CarrierTimeWindowBase] = Field(None, description="For delivery services. The specific delivery time window to book with the carrier. Query endpoint `/shipments/{id}/carrier/delivery` to get available time windows, or check Glueys portal for values you can hardcode.")
    book_collection: Optional[CarrierTimeWindowBase] = Field(None, description="For collection services. The specific collection time window to book with the carrier. Query endpoint `/shipments/{id}/carrier/collection` to get available time windows, or check Glueys portal for values you can hardcode.")
    label: Optional[LabelRequest] = Field(None, description="The label requested, including the size and type. Only applicable to services where a label is generated, for paperless services this is not required.")

class UpdateCollectionRequest(BaseModel):
    collection_time: Optional[CarrierTimeWindowBase] = Field(None, description="For collection services. The specific collection time window to book with the carrier. Query endpoint `/shipments/{id}/carrier/collection` to get available time windows, or check Glueys portal for values you can hardcode.")
    collection_address: Optional[DeliveryAddress] = Field(None, description="The address where the collection should take place. If not provided the address from the original booking will be used.")
    