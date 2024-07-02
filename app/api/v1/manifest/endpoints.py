from fastapi import APIRouter, Depends, status

from app.api.v1.common.headers import common_headers
from app.api.v1.manifest.models.get_manifest_response import GetManifestResponse
from app.api.v1.manifest.models.manifest_shipment_request import ManifestShipmentRequest
from app.api.v1.manifest.models.manifest_shipment_response import ManifestShipmentResponse
from app.api.v1.manifest.models.manifest_shipments_request import ManifestShipmentsRequest
from app.api.v1.manifest.models.manifest_shipments_response import ManifestShipmentsResponse

from app.api.v1.manifest.http_responses.payloads import http_create_manifest_response, http_get_manifest_response

router = APIRouter()

@router.post("/shipments/{id}/manifests", description="Endpoint to manifest a previously created shipment and get related carrier documents", summary="Manifest Single Shipment", responses=http_create_manifest_response, status_code=status.HTTP_201_CREATED)
async def shipment_manifest(id: str, payload: ManifestShipmentRequest, headers: dict = Depends(common_headers)) -> ManifestShipmentResponse:
    return

@router.get("/shipments/{id}/manifests/{manifest_id}", description="Endpoint to get carrier documents and related information from a previously manifested shipment", summary="Get Manifest for Single Shipment", responses=http_get_manifest_response)
async def shipment_manifest_get(id: str, manifest_id: str, headers: dict = Depends(common_headers)) -> ManifestShipmentResponse:
    return

@router.post("/manifests", description="Endpoint to batch manifest several shipments simultaneously", summary="Batch Manifest Shipments", responses=http_create_manifest_response, status_code=status.HTTP_201_CREATED)
async def manifests(payload: ManifestShipmentsRequest, headers: dict = Depends(common_headers)) -> ManifestShipmentsResponse:
    return

@router.get("/manifests/{id}", description="Endpoint to get carrier documents and related information from previously batch manifest of shipments", summary="Get Batch Manifest", responses=http_get_manifest_response)
async def manifests_get(id: str, headers: dict = Depends(common_headers)) -> GetManifestResponse:
    return
