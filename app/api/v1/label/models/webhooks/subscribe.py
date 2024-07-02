
from pydantic import BaseModel, Field

class SubscribeShipmentWebhook(BaseModel):
    endpoint: str = Field(..., description="The URL to your endpoint that will receive the webhook messages.")