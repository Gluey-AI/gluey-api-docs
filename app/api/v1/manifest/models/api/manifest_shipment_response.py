from typing import Optional
from pydantic import Field

from app.api.v1.common.models.base_models import Document
from app.api.v1.common.models.base_manifest import ManifestBaseModel

class ManifestShipmentResponse(ManifestBaseModel):
    """The response model for manifesting / close-out incl any documents returned from carrier."""
    id: str = Field(..., description="The Gluey manifest id related to the shipment.")
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")