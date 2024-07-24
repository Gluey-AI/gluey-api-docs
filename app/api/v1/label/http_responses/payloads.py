from app.api.v1.common.http_responses.payloads import http_502_response

# booking_success_example = BookingResponse(
#     carrier_collection_id=generate_custom_uuid(8),
#     carrier_payment_url="https://checkout.stripe.com/pay/123e4567-e89b-12d3-a456-426614174000?amount=53.50&currency=USD",
#     carrier_mangement_url="https://carrier.com/management/123e4567-e89b-12d3-a456-426614174000"
# )

# booking_success_example_no_payment = BookingResponse(
#     carrier_collection_id=generate_custom_uuid(8),
#     carrier_payment_url=None,
#     carrier_meta_data=[
#         MetaData(
#             key="vehicle_type",
#             value="van"
#         )
#     ]
# )

# booking_response_examples = {
#     "success": {
#         "summary": "Booking Response - Success",
#         "description": "Example response when the booking of a collection was successful but customer still has a pending payment with the carrier.",
#         "value": booking_success_example.model_dump()
#     },
#     "success_no_payment": {
#         "summary": "Booking Response - Success - No Payment",
#         "description": "Example response when the booking of a collection was successful, and no further payment is required.",
#         "value": booking_success_example_no_payment.model_dump()
#     }
# }

# http_responses_booking = {
#     201: {
#         "description": "Booking of collection was successful",
#         "content": {
#             "application/json": {
#                 "examples": booking_response_examples
#             }
#         }
#     },
#     400: {
#         "description": "Bad Request - Payload malformed",
#         "content": {
#             "application/json": {
#                 "example": {
#                     "detail": "Payload malformed."
#                 }
#             }
#         }
#     },
#     401: {
#         "description": "Unauthorized",
#         "content": {
#             "application/json": {
#                 "example": {
#                     "detail": "Not authenticated."
#                 }
#             }
#         }
#     },
#     403: {
#         "description": "Forbidden",
#         "content": {
#             "application/json": {
#                 "example": {
#                     "detail": "Not authorized to access this shipment."
#                 }
#             }
#         }
#     },
#     406: {
#         "description": "Not Acceptable - JSON only responses supported",
#         "content": {
#             "application/json": {
#                 "example": {
#                     "detail": "The requested resource is not available in a format that would be acceptable according to the Accept headers sent in the request."
#                 }
#             }
#         }
#     },
#     500: {
#         "description": "Internal Server Error",
#         "content": {
#             "application/json": {
#                 "example": {
#                     "detail": "Unfortunately something went wrong whilst processing your request. Please try again later."
#                 }
#             }
#         }
#     },
#     502: http_502_response
# }


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
                201: {
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