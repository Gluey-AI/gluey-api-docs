from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document, MetaData

class ShipmentInfo(BaseModel):
    shipment_id: str = Field(..., description="Glueys unique identifier for the shipment.")
    carrier_manifest_id: Optional[str] = Field(None, description="Any id returned from the carrier API related to the individual shipment. For most carriers this will be empty.")
    shipment_documents: Optional[list[Document]] = Field([], description="Any documents returned from the carrier API for this particular shipment. For most carriers this will be empty.")
    carrier_meta_data: Optional[list[MetaData]] = Field([], description="Any meta data returned from the carrier API related to this specific shipment. For most carriers this will be empty.")

class GetManifestResponse(BaseModel):
    """The response model for manifesting / close-out incl any documents returned from carrier."""
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")
    carrier_meta_data: Optional[list[MetaData]] = Field([], description="Any meta data returned from the carrier API related to this manifest.")
    carrier_id: str = Field(..., description="Glueys ID that identifies the carrier in our system, e.g. 'poste_italiane', 'yodel'. The Gluey ID of the carrier as found in the library of carriers in Gluey.")
    carrier_manifest_id: Optional[str] = Field(None, description="Any manifest id returned from the carrier API that is related to the list of shipments included in this batch.")
    documents: Optional[list[Document]] = Field([], description="Any documents returned from the carrier API.")
    shipments: list[ShipmentInfo] = Field([], description="The shipment id including any manifest reference or documents from the carrier connected to an individual shipment.")