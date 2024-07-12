from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import GlueyApiServices
from app.api.v1.label.models.api.customs_clearance import CustomsClearance
from app.api.v1.label.models.api.dangerous_goods import ShipmentLevelDangerousGoods
from app.api.v1.label.models.base_models import CollectionTimeWindow, CommercialInvoice, LabelRequest
from app.api.v1.label.models.api.carrier_request import CarrierRequestModel
from app.api.v1.label.models.api.shipment_request import ShipmentRequestModel

class AdditionalDocuments(BaseModel):
    """The additional documents you can request Gluey to generate for a shipment"""
    commercial_invoice: Optional[CommercialInvoice] = Field(None, description="The details about the commercial invoice you wish Gluey to generate for the shipment.")

# This is the request model for the Gluey carrier operation TYPE3_CREATE_SHIPMENT_WITH_LABEL
# The request is both creating a shipment in Gluey, and creating a label.
class CreateShipmentWithLabelsDocumentsRequest(BaseModel):
    """The request model for creating a shipment and printing a label."""
    gluey_services: Optional[GlueyApiServices] = Field(None, description="Gluey convenience services you would like executed as part of the api calls, e.g. address correction, dimension conversion, weight conversion etc")
    carrier: CarrierRequestModel = Field(..., description="The parcel carrier that should move all the parcels.")
    label_request: LabelRequest = Field(..., description="The details about the label requested, including the size and type. Only applicable to services where a label is generated, for paperless services this is not required.")
    additional_document_request: Optional[AdditionalDocuments] = Field(None, description="The additional documents you can request Gluey to generate for a shipment")
    collection_times: Optional[list[CollectionTimeWindow]] = Field(None, description="A list of times when the shipment can be collected. How to use:\n- If you have a `specific collection time and date`, then provide a single collection time with only the `start` specified.\n- If you have a `single collection time window`, then provide a single collection time with both `start` and `end` specified.\n- If you have `multiple collection time windows` that are acceptable, and the carrier supports it, then provide multiple time windows where all have with both `start` and `end` specified.")
    dng_declaration: Optional[ShipmentLevelDangerousGoods] = Field(None, description="Optional. Shipment-level details are not mandatory for dangerous goods shipments, but `parcel-level` and `item-level` details are mandatory.")
    customs_clearance: Optional[CustomsClearance] = Field(None, description="Customs clearance details about the shipment. Only applicable to cross-border shipments.")
    shipment: ShipmentRequestModel = Field(..., description="The shipment details, including the parcels and their contents.")