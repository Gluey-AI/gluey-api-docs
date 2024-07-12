from fastapi import APIRouter, Body, Depends, Path, status

from app.api.v1.book.models.api.collection import BookingResponse, CollectionRequest, CollectionResponse
from app.api.v1.common.headers import common_headers

from app.api.v1.book.http.response_examples import http_responses_collection_times, http_responses_cancel, http_responses_booking
from app.api.v1.book.http.request_examples import collection_request_examples


router = APIRouter()

@router.post("/shipments/{id}/collection", description="Endpoint to request available collection times for when a carrier can collect a shipment.", summary="Request available Collection Dates", responses=http_responses_collection_times, status_code=status.HTTP_200_OK)
async def request_collection_dates(
    payload: CollectionRequest = Body(..., openapi_examples=collection_request_examples),
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> CollectionResponse:
    return

@router.post("/shipments/{id}/collection/{collection_id}/time/{time_id}", description="Endpoint to book a collection for a shipment for a specific date / time / time window.", summary="Book Collection", responses=http_responses_booking, status_code=status.HTTP_201_CREATED)
async def book_collection(
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    collection_id: str = Path(..., description="Glueys own unique identifier of a collection request for the shipment."),
    time_id: str = Path(..., description="Glueys own unique identifier of a date / time / time window from a collection request."),
    headers: dict = Depends(common_headers)) -> BookingResponse:
    return

@router.delete("/shipments/{id}/collection/{collection_id}", description="Endpoint to cancel a collection that is booked with the carrier.", summary="Cancel Collection", responses=http_responses_cancel, status_code=status.HTTP_204_NO_CONTENT)
async def cancel_collection(
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    collection_id: str = Path(..., description="Glueys own unique identifier of a collection request for the shipment."),
    headers: dict = Depends(common_headers)):
    return