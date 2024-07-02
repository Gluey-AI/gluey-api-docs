from pydantic import BaseModel, Field

class TrackShipmentsRequest(BaseModel):
    """The request model to get the latest status / tracking events for a list of shipments."""
    ids: str = Field([], description="A list of the IDs for the shipments to track. Up to 100 shipments can be tracked in the same request.")