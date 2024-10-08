from fastapi import APIRouter, Depends, Path

from app.api.v1.common.headers import common_headers
from app.api.v1.tracking.models.api.track_shipments_request import TrackShipmentsRequest
from app.api.v1.tracking.models.api.track_batch import BatchTrackShipment
from app.api.v1.tracking.models.api.track_single_shipment import TrackSingleShipment

from app.api.v1.tracking.http_responses.payloads import http_get_tracking_response

router = APIRouter()

@router.get("/shipments/{id}/track", description="Endpoint to fetch tracking events for a previously created shipment", summary="Track Single Shipment", responses=http_get_tracking_response)
async def shipment_track(id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)) -> TrackSingleShipment:
    return

@router.post("/track", description="Endpoint to batch track up to 100 shipments at the same time", summary="Batch Track Shipments", responses=http_get_tracking_response)
async def track(payload: TrackShipmentsRequest, headers: dict = Depends(common_headers)) -> list[BatchTrackShipment]:
    return