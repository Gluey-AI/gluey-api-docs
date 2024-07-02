from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document
from app.api.v1.label.models.shipment_response import ShipmentResponseModel

class CreateShipmentWithLabelsDocumentsResponse(BaseModel):
    """The response which contains the parcel labels, tracking numbers and barcodes."""
    shipment: ShipmentResponseModel = Field(..., description="The shipment details, including the parcels, tracking numbers, barcodes and the labels.")
    documents: Optional[list[Document]] = Field([], description="Any documents that were requested by Gluey and / or returned from the carrier API.")