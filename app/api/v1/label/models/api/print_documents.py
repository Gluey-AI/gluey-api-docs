from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import DocumentType, document_type_descriptions
from app.api.v1.common.utils import get_enum_description

class PrintDocumentsRequest(BaseModel):
    document_types: list[DocumentType] = Field(..., description=f"The types of documents you wish to generate. It can be one of the following:\n{get_enum_description(DocumentType, document_type_descriptions)}")