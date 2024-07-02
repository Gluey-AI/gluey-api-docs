from typing import Optional
from pydantic import BaseModel, Field

# This is the request model for the Gluey carrier operation TYPE4_MANIFEST_SHIPMENT
# The request triggering the manifest / close-out / pre-notice to the carrier for a list of shipments.
class ManifestShipmentsRequest(BaseModel):
    """The request model to perform manifesting / close-out towards the carrier."""
    uuid_ref: Optional[str] = Field(None, description="Your own unique identifier for the Manifest. This is useful for tracking and reconciliation.")
    shipment_ids: str = Field([], description="A list of the IDs for the shipments to manifest. These can be from different carriers.")