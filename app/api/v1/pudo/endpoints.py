from fastapi import APIRouter, Depends, Query

from app.api.v1.common.headers import common_headers
from app.api.v1.pudo.models.api.pudo import PudoPoint

from app.api.v1.pudo.http_responses.payloads import http_get_pudo_response

router = APIRouter()

@router.get("/pudo", description="Endpoint to fetch pudo points for a specific carrier / country.", summary="Get PUDO Points", responses=http_get_pudo_response)
async def pudo(headers: dict = Depends(common_headers), carrier_code: str = Query('', description="The gluey carrier code connected to the carrier you want to fetch pudo points for, e.g. 'dhl_express' etc."), iso_country: str = Query('', description="The ISO Alpha-2 ('GB') or ISO Alpha-3 ('GBR') country code.")) -> list[PudoPoint]:
    return