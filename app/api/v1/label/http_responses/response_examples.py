from app.api.v1.common.models.base_models import Dimensions, UnitOfMeasurement, UnitOfWeight, Weight
from app.api.v1.label.models.api.carrier import CarrierService, CarrierServiceType, Direction, GlueyValueAddingServiceClass, Region, ValueAddingService, CarrierServiceRestrictions
from app.api.v1.label.models.api.collection import CarrierCollectionTimeWindow, CarrierServiceCollectionDates
from app.api.v1.common.http_responses.payloads import http_502_response
from app.api.v1.common.utils import generate_uuid, generate_short_uuid, generate_custom_uuid

collection_services = [
    CarrierServiceCollectionDates(
        carrier_service_id="2CPR",
        carrier_service_name="Xpect Medium Return",
        collection_time_windows=[
            CarrierCollectionTimeWindow(
                start="2024-07-12T09:00:00-04:00",
                end="2024-07-12T12:00:00-04:00",
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-12T14:30:00-04:00",
                end="2024-07-12T17:30:00-04:00",
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T09:00:00-04:00",
                end="2024-07-13T12:00:00-04:00"
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T14:30:00-04:00",
                end="2024-07-13T17:30:00-04:00"
            )
        ]
    ),
    CarrierServiceCollectionDates(
        carrier_service_id="2VPR",
        carrier_service_name="Xpect Large Return",
        collection_time_windows=[
            CarrierCollectionTimeWindow(
                start="2024-07-12T09:00:00-04:00",
                end="2024-07-12T12:00:00-04:00",
                cost=3.45,
                cost_currency="GBP"
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-12T14:30:00-04:00",
                end="2024-07-12T17:30:00-04:00",
                cost=3.45,
                cost_currency="GBP"
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T09:00:00-04:00",
                end="2024-07-13T12:00:00-04:00"
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T14:30:00-04:00",
                end="2024-07-13T17:30:00-04:00"
            )
        ]
    )
]

collection_services_day = [
    CarrierServiceCollectionDates(
        carrier_service_id="EXP",
        carrier_service_name="Express",
        collection_time_windows=[
            CarrierCollectionTimeWindow(
                start="2024-07-12T08:00:00-04:00",
                end="2024-07-12T17:00:00-04:00",
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T08:00:00-04:00",
                end="2024-07-13T17:00:00-04:00"
            )
        ]
    ),
    CarrierServiceCollectionDates(
        carrier_service_id="PRCSEL",
        carrier_service_name="Premium Select",
        collection_time_windows=[
            CarrierCollectionTimeWindow(
                start="2024-07-12T08:00:00-04:00",
                end="2024-07-12T17:00:00-04:00",
            ),
            CarrierCollectionTimeWindow(
                start="2024-07-13T08:00:00-04:00",
                end="2024-07-13T17:00:00-04:00"
            )
        ]
    )
]

# booking_success_example = BookingResponse(
#     collection_status=CollectionStatus.BOOKED,
#     carrier_collection_id=generate_custom_uuid(8),
#     paymentUrl="https://checkout.stripe.com/pay/123e4567-e89b-12d3-a456-426614174000?amount=53.50&currency=USD",
# )

# booking_success_example_no_payment = BookingResponse(
#     collection_status=CollectionStatus.BOOKED,
#     carrier_collection_id=generate_custom_uuid(8),
#     paymentUrl=None,
# )

collection_response_examples = {
    "am_pm": {
        "summary": "Collection Response - AM / PM",
        "description": "Example response when the carrier support both AM and PM collection times.",
        "value": collection_services
    },
    "whole_day": {
        "summary": "Collection Response - Dates only",
        "description": "When the carrier only supports collection dates, but no time window, the entire day is the collection window.",
        "value": collection_services_day
    }
}

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

carrier_services = [
    CarrierService(
        carrier_service_id="2CPR",
        name="Xpect Medium Return",
        direction=Direction.RETURN,
        region=Region.DOMESTIC,
        service_type=CarrierServiceType.PICKUP_DROPOFF_POINT
    ),
    CarrierService(
        carrier_service_id="2VPR",
        name="Xpect Large Return",
        direction=Direction.RETURN,
        region=Region.DOMESTIC,
        service_type=CarrierServiceType.COLLECTION_AT_HOME,
        restrictions=CarrierServiceRestrictions(
            max_weight=Weight(value=30, unit=UnitOfWeight.KG),
            max_dims=Dimensions(length=100, width=100, height=210, unit=UnitOfMeasurement.CM)
        ),
        value_adding_services=[
            ValueAddingService(
                id="2VPR-HZ",
                name="Add on for dangerous goods",
                gluey_classification=GlueyValueAddingServiceClass.DNG_HAZMAT,
            )
        ]
    )
]

service_availability_response_examples = {
    "success": {
        "summary": "Carrier services available - including value adding services",
        "description": "Example response when carrier services are available for the shipment - including value adding services.",
        "value": carrier_services
    }
}

http_responses_service_availability = {
    200: {
        "description": "Carrier Services Found",
        "content": {
            "application/json": {
                "examples": service_availability_response_examples
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
        "description": "Not Acceptable - JSON only responses supported",
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

http_responses_collection_times = {
    200: {
        "description": "Collection time request succeeded",
        "content": {
            "application/json": {
                "examples": collection_response_examples
            }
        }
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
        "description": "Not Acceptable - JSON only responses supported",
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

http_responses_cancel = {
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
        "description": "Not Acceptable - JSON only responses supported",
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