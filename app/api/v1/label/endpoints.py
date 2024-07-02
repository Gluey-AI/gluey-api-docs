from fastapi import APIRouter, Depends, Query, status

from app.api.v1.common.headers import common_headers
from app.api.v1.common.models.base_models import Document
from app.api.v1.label.models.base_models import LabelFormat
from app.api.v1.label.models.api.create_shipment_request import CreateShipmentRequest
from app.api.v1.label.models.api.create_shipment_with_labels_request import CreateShipmentWithLabelsDocumentsRequest
from app.api.v1.label.models.api.create_shipment_with_labels_response import CreateShipmentWithLabelsDocumentsResponse
from app.api.v1.label.models.api.get_labels_for_shipment_response import GetLabelsForShipmentResponse
from app.api.v1.label.models.api.print_documents_for_shipment_request import PrintDocumentsForShipmentRequest
from app.api.v1.label.models.api.shipment import Shipment
from app.api.v1.label.models.api.shipment_only_response import ShipmentOnlyResponseModel

from app.api.v1.label.http_responses.payloads import http_create_shipment_response, http_get_shipment_response, http_delete_shipment_response, http_get_labels_response, http_get_documents_response, http_create_shipment_labels_response


router = APIRouter()

@router.post("/shipments", description="Endpoint to create a shipment in Gluey without printing a label.", summary="Create Shipment", responses=http_create_shipment_response, status_code=status.HTTP_202_ACCEPTED)
async def create_shipment(payload: CreateShipmentRequest, headers: dict = Depends(common_headers)) -> ShipmentOnlyResponseModel:
    return

@router.get("/shipments/{id}", description="Endpoint to get a previously created Shipment.", summary="Get Shipment", responses=http_get_shipment_response)
async def get_shipment(id: str, headers: dict = Depends(common_headers)) -> Shipment:
    return

@router.delete("/shipments/{id}", description="Endpoint to cancel / delete a previously created shipment. Allowed until manifesting has taken place.", summary="Cancel Shipment", responses=http_delete_shipment_response, status_code=status.HTTP_204_NO_CONTENT)
async def delete_shipment(id: str, headers: dict = Depends(common_headers)):
    return

@router.get("/shipments/{id}/labels", description="Endpoint to fetch labels for all parcels in a shipment.", summary="Get Labels for Shipment", responses=http_get_labels_response)
async def get_labels(id: str, headers: dict = Depends(common_headers), format: LabelFormat = Query(LabelFormat.ZPL200, description="The format of the labels you want to fetch. Not applicable to paperless services.")) -> GetLabelsForShipmentResponse:
    return

@router.post("/shipments/{id}/documents", description="Endpoint to fetch all documents related to a shipment, or asking Gluey to generate some for you.", summary="Generate Documents for Shipment", responses=http_get_documents_response)
async def generate_documents(id: str, payload: PrintDocumentsForShipmentRequest, headers: dict = Depends(common_headers)) -> list[Document]:
    return

@router.post("/shipment_with_labels_documents", description="Endpoint to create a shipment, print labels for all parcels, and retrieve all documents related to the shipment.", summary="Create Shipment with Labels and Documents", responses=http_create_shipment_labels_response, status_code=status.HTTP_201_CREATED)
async def shipment_labels_documents(payload: CreateShipmentWithLabelsDocumentsRequest, headers: dict = Depends(common_headers)) -> CreateShipmentWithLabelsDocumentsResponse:
    return
