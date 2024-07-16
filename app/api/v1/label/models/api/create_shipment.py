from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import GlueyApiServices
from app.api.v1.label.models.api.base_shipment_request import BaseShipmentRequestModel
from app.api.v1.label.models.api.carrier_request import BaseCarrierRequestModel

class CreateShipmentRequest(BaseModel):
    gluey_services: Optional[GlueyApiServices] = Field(None, description="Gluey convenience services you would like executed as part of the api calls, e.g. address correction, dimension conversion, weight conversion etc")
    carrier: BaseCarrierRequestModel = Field(..., description="The carrier that should move this parcel.")
    shipment: BaseShipmentRequestModel = Field(..., description="The shipment details, including the parcels and their contents.")