from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document, MetaData

class ShipmentManifestInfo(BaseModel):
    id: str = Field(..., description="The ID of the shipment that was manifested.")
    carrier_manifest_id: Optional[str] = Field(..., description="Any id returned from the carrier API related to the individual shipment. For most carriers this will be empty.")
    shipment_documents: Optional[list[Document]] = Field([], description="Any documents returned from the carrier API for this particular shipment. For most carriers this will be empty.")
    meta_data: Optional[list[MetaData]] = Field([], description="Any meta data returned from the carrier API related to this specific shipment. For most carriers this will be empty.")

class GlueyManifest(BaseModel):
    id: str = Field(..., description="The Gluey manifest id related to the carrier manifest.")
    carrier_meta_data: Optional[list[MetaData]] = Field([], description="Any meta data returned from the carrier API related to this manifest.")
    carrier_code: str = Field(..., description="The code of the carrier the manifest document is connected to, e.g. 'ups', 'gls_logistics', 'dhl_express'.")
    carrier_manifest_id: Optional[str] = Field(..., description="Any manifest id returned from the carrier API that is related to the list of shipments included in this batch.")
    documents:Optional[list[Document]] = Field([], description="Any documents returned from the carrier API.")
    shipments: list[ShipmentManifestInfo] = Field([], description="The shipment id including any manifest reference or documents from the carrier connected to an individual shipment.")

class ManifestShipmentsResponse(BaseModel):
    """The response model for manifesting / close-out incl any documents returned from carrier."""
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")
    manifests: Optional[list[GlueyManifest]] = Field([], description="Manifest information returned by the carrier. This can include manifest id, documents or other types of meta data from the carrier API.")