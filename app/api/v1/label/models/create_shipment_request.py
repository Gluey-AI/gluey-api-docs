from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import GlueyApiServices
from app.api.v1.label.models.carrier_request import CarrierRequestModel
from app.api.v1.label.models.shipment_request import ShipmentRequestModel

class CreateShipmentRequest(BaseModel):
    """The request model for creating a shipment only, without printing a label."""
    gluey_services: Optional[GlueyApiServices] = Field(None, description="Gluey convenience services you would like executed as part of the api calls, e.g. address correction, dimension conversion, weight conversion etc")
    carrier: CarrierRequestModel = Field(..., description="The parcel carrier that should move all the parcels.")
    shipment: ShipmentRequestModel = Field(..., description="The shipment details, including the parcels and their contents.")