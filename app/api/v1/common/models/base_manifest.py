from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Document

class ManifestBaseModel(BaseModel):
    """A manifest / close-out call incl any documents returned from carrier."""
    carrier_manifest_id: Optional[str] = Field(None, description="Any id returned from the carrier API.")
    documents: Optional[list[Document]] = Field([], description="Any documents that were requested by Gluey and / or returned from the carrier API.")