from fastapi import APIRouter, Depends, Query

from app.api.v1.common.headers import common_headers
from app.api.v1.pudo.models.api.pudo import PudoPoint

from app.api.v1.pudo.http_responses.payloads import http_get_pudo_response

router = APIRouter()

@router.get("/pudo", description="Endpoint to fetch pudo points for a specific carrier / country.", summary="PUDO Points", responses=http_get_pudo_response)
async def pudo(headers: dict = Depends(common_headers), carrier_id: str = Query(..., description="Glueys ID that identifies the carrier in our system, e.g. 'poste_italiane', 'yodel'. The Gluey ID of the carrier as found in the library of carriers in Gluey."), iso_country: str = Query('', description="The ISO Alpha-2 ('GB') or ISO Alpha-3 ('GBR') country code."), page: int = Query(1, description="The page number related to the pudo point retrieval")) -> list[PudoPoint]:
    return