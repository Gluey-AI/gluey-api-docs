
from enum import Enum
from typing import Annotated

from fastapi import HTTPException, Header, status

class APIVersion(str, Enum):
    v1 = "v1"
    """API Version 1 of the Gluey API"""

async def common_headers(
    x_key: Annotated[str, Header(..., description="The API key that was assigned by Gluey", example="gl-acc-flsjukcKHJF6iHFi66666f3r99kv")],
    x_version: Annotated[APIVersion, Header(..., description="The API version to use", example="v1")]
):
    if not x_key:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="x-key header missing")
    if not x_version:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="x-version header missing")
    return {"x-key": x_key, "x-version": x_version}