from fastapi import APIRouter, Depends, status

from app.api.v1.common.headers import common_headers
from app.api.v1.label.models.webhooks.subscribe import SubscribeShipmentWebhook
from app.api.v1.label.models.webhooks.update_shipment import UpdateShipmentEvent

webhook_router = APIRouter()

@webhook_router.post("/webhook/shipment", summary="Update Shipment Webhook", description="How the webhook messages look like that you will receive from Gluey", status_code=status.HTTP_200_OK)
async def receive_webhook(payload: UpdateShipmentEvent):
    return

webhook_subscription_router = APIRouter()

@webhook_subscription_router.post("/accounts/{account_number}/webhooks/shipment/subscriptions", description="Endpoint to subscribe your account to a webhook from Gluey. ", summary="Subscribe to Update Shipment Webhook", status_code=status.HTTP_201_CREATED)  
async def create_subscription(account_number: str, payload: SubscribeShipmentWebhook, headers: dict = Depends(common_headers)):
    return

@webhook_subscription_router.delete("/accounts/{account_number}/webhooks/shipment/subscriptions", description="Endpoint to delete your subscription for shipment updates from Gluey. ", summary="Delete Subscription to Update Shipment Webhook", status_code=status.HTTP_204_NO_CONTENT)  
async def delete_subscription(account_number: str, headers: dict = Depends(common_headers)):
    return