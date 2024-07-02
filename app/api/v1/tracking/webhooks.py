from fastapi import APIRouter, Depends, status

from app.api.v1.common.headers import common_headers
from app.api.v1.tracking.models.webhooks.subscribe import SubscribeTrackingWebhook
from app.api.v1.tracking.models.webhooks.tracking_event import TrackingWebhookEvent


webhook_router = APIRouter()

@webhook_router.post("/webhook/tracking", summary="Tracking Event Webhook", description="How the webhook messages with Tracking Events will look like that you receive from Gluey.", status_code=status.HTTP_200_OK)
async def receive_webhook(payload: list[TrackingWebhookEvent]):
    return

webhook_subscription_router = APIRouter()

@webhook_subscription_router.post("/accounts/{account_number}/webhooks/tracking/subscriptions", description="Endpoint to subscribe your account to a webhook from Gluey. ", summary="Subscribe to Tracking Event Webhook", status_code=status.HTTP_201_CREATED)  
async def create_subscription(account_number: str, payload: SubscribeTrackingWebhook, headers: dict = Depends(common_headers)):
    return

@webhook_subscription_router.delete("/accounts/{account_number}/webhooks/tracking/subscriptions", description="Endpoint to delete your subscription for tracking events from Gluey. ", summary="Delete Subscription to Tracking Event Webhook", status_code=status.HTTP_204_NO_CONTENT)  
async def delete_subscription(account_number: str, headers: dict = Depends(common_headers)):
    return
