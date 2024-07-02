
from pydantic import BaseModel, Field

class SubscribeTrackingWebhook(BaseModel):
    endpoint: str = Field(..., description="The URL to your endpoint that will receive the webhook messages.")