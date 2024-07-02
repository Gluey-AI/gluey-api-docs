from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document

class ManifestShipmentResponse(BaseModel):
    """The response model for manifesting / close-out incl any documents returned from carrier."""
    id: str = Field(..., description="The Gluey manifest id related to the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")
    carrier_manifest_id: Optional[str] = Field(..., description="Any id returned from the carrier API.")
    documents: Optional[list[Document]] = Field([], description="Any documents that were requested by Gluey and / or returned from the carrier API.")