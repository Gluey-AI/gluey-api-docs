from typing import Optional
from pydantic import BaseModel, Field

class ManifestShipmentRequest(BaseModel):
    """The response model for manifesting / close-out incl any documents returned from carrier."""
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")