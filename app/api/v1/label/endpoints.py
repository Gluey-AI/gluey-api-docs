from fastapi import APIRouter, Body, Depends, Path, Query, status

from app.api.v1.common.headers import common_headers
from app.api.v1.common.models.base_models import Document
from app.api.v1.label.models.api.base_shipment_response import BaseShipmentResponseModel
from app.api.v1.label.models.api.carrier import CarrierService
from app.api.v1.label.models.api.collection import CarrierServiceCollectionDates, CarrierServiceDeliveryDates, CarrierServiceTransitTime, CollectionRequest, DeliveryRequest, ServiceAvailabilityRequest, TransitTimeRequest
from app.api.v1.label.models.api.create_shipment import CreateShipmentRequest
from app.api.v1.label.models.api.print_label import CollectionBookingResponse, PrintAndBookRequest, PrintAndBookSyncResponse, PrintLabelRequest, PrintLabelSyncResponse, UpdateCollectionRequest
from app.api.v1.label.models.api.print_documents import PrintDocumentsRequest
from app.api.v1.label.models.api.shipment import Shipment

from app.api.v1.label.http_responses.payloads import http_create_shipment_response, http_get_shipment_response, http_delete_shipment_response, http_get_labels_response, http_get_documents_response
from app.api.v1.label.http_responses.request_examples import collection_request_examples, service_availability_request_examples, delivery_request_examples
from app.api.v1.label.http_responses.response_examples import http_responses_cancel, http_responses_collection_times, http_responses_service_availability, http_responses_delivery_times
from app.api.v1.label.models.api.update_shipment import UpdateShipmentRequest


router = APIRouter()

@router.post("/shipments", description="Endpoint to create a shipment synchronous in Gluey.", summary="Create Shipment Sync", responses=http_create_shipment_response, status_code=status.HTTP_201_CREATED)
async def create_shipment(payload: CreateShipmentRequest, headers: dict = Depends(common_headers)) -> BaseShipmentResponseModel:
    return

@router.get("/shipments/{id}", description="Endpoint to get a previously created Shipment.", summary="Get Shipment", responses=http_get_shipment_response)
async def get_shipment(id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)) -> Shipment:
    return

# @router.put("/shipments/{id}", description="Endpoint to update a previously created shipment.", summary="Update Shipment", status_code=status.HTTP_200_OK)
# async def update_shipment(payload: UpdateShipmentRequest, id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)):
#     return

# @router.delete("/shipments/{id}", description="Endpoint to cancel / delete a previously created shipment.", summary="Cancel Shipment", responses=http_delete_shipment_response, status_code=status.HTTP_204_NO_CONTENT)
# async def delete_shipment(id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)):
#     return


@router.post("/shipments/{id}/carrier/services", description="Endpoint to check what carrier services are available in Gluey for a specific shipment.", summary="Check Service Availability", tags=['Service Availability'], responses=http_responses_service_availability, status_code=status.HTTP_200_OK)
async def service_availability(
    payload: ServiceAvailabilityRequest = Body(..., openapi_examples=service_availability_request_examples),
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> list[CarrierService]:
    return

@router.post("/shipments/{id}/carrier/collection", description="Endpoint to request all available collection time windows for when a carrier can collect a shipment.", summary="Check Collection Dates", tags=['Service Availability'],responses=http_responses_collection_times, status_code=status.HTTP_200_OK)
async def request_collection_dates(
    payload: CollectionRequest = Body(..., openapi_examples=collection_request_examples),
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> list[CarrierServiceCollectionDates]:
    return

@router.post("/shipments/{id}/carrier/delivery", description="Endpoint to request all available delivery time windows for when a carrier can delivery a shipment.", summary="Check Delivery Dates", tags=['Service Availability'], responses=http_responses_delivery_times, status_code=status.HTTP_200_OK)
async def request_delivery_dates(
    payload: DeliveryRequest = Body(..., openapi_examples=delivery_request_examples),
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> list[CarrierServiceDeliveryDates]:
    return

@router.post("/shipments/{id}/carrier/transit-times", description="Endpoint to check available transit times for the carrier.", summary="Check Transit Times", tags=['Service Availability'], status_code=status.HTTP_200_OK)
async def request_transit_times(
    payload: TransitTimeRequest,
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> list[CarrierServiceTransitTime]:
    return

@router.post("/shipments/{id}/labels", description="Endpoint to print labels synchronous for all parcels in a shipment, and optionally, book a collection date and / or delivery date.", summary="Print Labels and Book Collection Sync", tags=['Print & Book'],responses=http_get_labels_response, status_code=status.HTTP_201_CREATED)
async def print_labels_book_sync(request: PrintAndBookRequest, id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)) -> PrintAndBookSyncResponse:
    return

@router.post("/shipments/{id}/documents", description="Endpoint to print all documents related to a shipment", summary="Print Documents", tags=['Print & Book'], responses=http_get_documents_response)
async def generate_documents(payload: PrintDocumentsRequest, id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)) -> list[Document]:
    return

@router.post("/shipments/{id}/labels/async", description="Endpoint to have Gluey print labels in the background. Printed labels will be pushed via webhook subscribers when available.", summary="Print Labels Async", tags=['Print & Book'], status_code=status.HTTP_202_ACCEPTED)
async def print_labels_async(request: PrintLabelRequest, id: str = Path(..., description="Glueys own unique identifier of the shipment"), headers: dict = Depends(common_headers)):
    return

# @router.post("/shipments/{id}/collection", description="Collection services only. Endpoint to print labels and book a collection date for a shipment.", summary="Print Labels and Book Collection Sync", tags=['Collection'], status_code=status.HTTP_201_CREATED)
# async def book_collection(
#     payload: PrintAndBookRequest,
#     id: str = Path(..., description="Glueys own unique identifier of the shipment"),
#     headers: dict = Depends(common_headers)) -> PrintAndBookSyncResponse:
#     return

@router.put("/shipments/{id}/collection", description="Endpoint to reschedule the collection of a shipment.", summary="Reschedule Collection", tags=['Manage Bookings'], status_code=status.HTTP_201_CREATED)
async def book_collection(
    payload: UpdateCollectionRequest,
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)) -> CollectionBookingResponse:
    return

@router.delete("/shipments/{id}/collection", description="Endpoint to cancel a collection that is booked with the carrier.", summary="Cancel Collection", tags=['Manage Bookings'], responses=http_responses_cancel, status_code=status.HTTP_204_NO_CONTENT)
async def cancel_collection(
    id: str = Path(..., description="Glueys own unique identifier of the shipment"),
    headers: dict = Depends(common_headers)):
    return