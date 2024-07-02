http_get_pudo_response = {
                200: {
            "description": "Pudo points found",
            "content": {
                "application/json": {
                    "example": {
                    }
                }
            },
            "headers": {
                "x-total-count": {
                    "description": "The total number of pudo points found",
                    "schema": {
                        "type": "integer",
                        "example": 15311
                    }
                },
                "x-next-page": {
                    "description": "The next page / batch of pudo points to retrieve",
                    "schema": {
                        "type": "string",
                        "example": "/pudo?carrier_code=dhl_express&iso_country=gb&page=3",
                        "format": "uri"
                    }
                },
                "x-prev-page": {
                    "description": "The previous page / batch of pudo points retrieved",
                    "schema": {
                        "type": "string",
                        "example": "/pudo?carrier_code=dhl_express&iso_country=gb&page=1",
                        "format": "uri"
                    }
                },
                "x-last-updated": {
                    "description": "The last time the pudo points were updated for this carrier / country",
                    "schema": {
                        "type": "string",
                        "format": "date-time",
                        "example": "2021-01-01T00:00:00Z"
                    }
                }
            }
        },
                204: {
            "description": "No pudo points available for carrier / country"
        },
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Not authenticated."
                    }
                }
            }
        },
        403: {
            "description": "Forbidden",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Not authorized to access pudo points for this carrier / country."
                    }
                }
            }
        },
                500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Unfortunately something went wrong whilst processing your request. Please try again later."
                    }
                }
            }
        }
    }