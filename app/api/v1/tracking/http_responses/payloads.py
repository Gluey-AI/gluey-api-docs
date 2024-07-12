http_get_tracking_response = {
                200: {
            "description": "Tracking events found",
            "content": {
                "application/json": {
                    "example": {
                    }
                }
            },
            "headers": {
                "x-last-updated": {
                    "description": "The last time the tracking events were updated for this carrier / country",
                    "schema": {
                        "type": "string",
                        "format": "date-time",
                        "example": "2021-01-01T00:00:00Z"
                    }
                }
            }
        },
                204: {
            "description": "No tracking events available for Shipment"
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
                        "detail": "Not authorized to access tracking for this / these shipment(s)."
                    }
                }
            }
        },
        404: {
            "description": "Shipment Not Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Shipment not found."
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