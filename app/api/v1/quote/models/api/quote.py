from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import BaseAddress, Dimensions, Weight

class QuoteParcel(BaseModel):
    """Class representing a parcel in the shipment."""
    id: str = Field(..., description="Glueys unique identifier for the parcel.")
    weight: Weight = Field(..., description="The total weight of the parcel. If left empty, Gluey will calculate the weight based on the items in the parcel.")
    dimensions: Optional[Dimensions] = Field(None, description="The dimensions of the parcel.")

class QuoteRequest(BaseModel):
    """Class representing a shipment being quoted."""
    carrier_service_id: str = Field(..., description="Glueys ID of the carrier service as found in our carrier library, e.g. 'standard_ground', 'express', 'home_delivery'.")
    from_address: BaseAddress = Field(..., description="The address of the sender / shipper / consignor. Also the address where to collect.")
    to_address: BaseAddress = Field(..., description="The address of the recipient / receiver / consignee to where the shipment is delivered")
    parcels: list[QuoteParcel] = Field([], description="A list of parcels included in the shipment")

class QuotePrice(BaseModel):
    """Class representing the price details of the quote."""
    currency: str = Field(..., description="The currency of the quoted price, e.g., USD, EUR.")
    amount: float = Field(..., description="The total amount of the quoted price.")

class EstimatedDelivery(BaseModel):
    """Class representing the estimated delivery details."""
    delivery_date: str = Field(..., description="The estimated delivery date in ISO 8601 format (YYYY-MM-DD).")
    delivery_time: Optional[str] = Field(None, description="The estimated delivery time in ISO 8601 format (HH:MM:SS).")

class QuoteResponse(BaseModel):
    """Class representing the response of a quote request."""
    id: str = Field(..., description="Gluey unique identifier for the quote.")
    carrier_id: str = Field(..., description="The Carriers unique ID of the Quote.")
    price: QuotePrice = Field(..., description="The price details of the quote.")
    estimated_delivery: Optional[EstimatedDelivery] = Field(None, description="The estimated delivery details.")