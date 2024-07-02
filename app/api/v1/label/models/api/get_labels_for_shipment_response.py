from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document
from app.api.v1.label.models.api.shipment_response import ShipmentResponseModel

class GetLabelsForShipmentResponse(BaseModel):
    """The labels that was created for the previously generated shipment."""
    shipment: ShipmentResponseModel = Field(..., description="The shipment details, including the parcels, tracking numbers, barcodes and the labels.")
    documents: Optional[list[Document]] = Field([], description="Any documents apart from the label that were returned from the carrier API.")