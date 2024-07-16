from app.api.v1.common.http_responses.payloads import http_502_response

http_create_shipment_response = {
        201: {
            "description": "Shipment created in Gluey",
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
                        "detail": "Not authorized to access this shipment."
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
        }
    }

http_get_shipment_response = {
                200: {
            "description": "Shipment found"
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
                        "detail": "Not authorized to access this shipment."
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
        }
    }

http_delete_shipment_response = {
                204: {
            "description": "Shipment deleted successfully"
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
                        "detail": "Not authorized to delete this shipment."
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

http_get_labels_response = {
                200: {
            "description": "Labels printed successfully"
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
                        "detail": "Not authorized to access labels for this shipment."
                    }
                }
            }
        },
        404: {
            "description": "Shipment / Labels Not Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Shipment / Labels not found."
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
        502: http_502_response
    }

http_get_documents_response = {
                200: {
            "description": "Documents found"
        },
                204: {
            "description": "No documents available for Shipment"
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
                        "detail": "Not authorized to access labels for this shipment."
                    }
                }
            }
        },
        404: {
            "description": "Shipment / Documents Not Found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Shipment / Documents not found."
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


http_create_shipment_labels_response = {
                201: {
            "description": "Shipment with Labels and Documents created successfully",
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
                        "detail": "Not authorized to access labels for this shipment."
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
                502: http_502_response
    }