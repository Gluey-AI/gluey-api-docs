from pydantic import BaseModel, Field

from app.api.v1.pudo.models.api.pudo import PudoPoint

class GetPudoPointsResponse(BaseModel):
    """The response model to get all the pudo points for a carrier / country."""
    pudo_points: list[PudoPoint] = Field([], description="A list of PUDO points for the carrier / country.")
