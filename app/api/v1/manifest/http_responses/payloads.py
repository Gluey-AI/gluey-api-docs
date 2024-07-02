from app.api.v1.common.http_responses.payloads import carrier_api_error

http_create_manifest_response = {
                201: {
            "description": "Manifest created for Shipment"
        },
                400: {
            "description": "Bad Request - Payload malformed",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Payload malformed."
                    }
                }
            }
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
                        "detail": "Not authorized to manifest this shipment."
                    }
                }
            }
        },
        406: {
            "description": "Not Acceptable - Json only responses supported",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "The requested resource is not available in a format that would be acceptable according to the Accept headers sent in the request."
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
        },
                502: {
            "description": "Carrier API Error",
            "content": {
                "application/json": {
                    "example": carrier_api_error
                }
            }
        }
    }

http_get_manifest_response = {
                200: {
            "description": "Manifest found",
            "content": {
                "application/json": {
                    "example": {
                    }
                }
            }
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
                        "detail": "Not authorized to access this manifest."
                    }
                }
            }
        },
        404: {
            "description": "Manifest Not Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Manifest not found."
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