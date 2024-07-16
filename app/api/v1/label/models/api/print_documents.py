from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.label.models.base_models import CommercialInvoice

class PrintDocumentsRequest(BaseModel):
    commercial_invoice: Optional[CommercialInvoice] = Field(None, description="The details about the commercial invoice you wish Gluey to generate for the shipment.")