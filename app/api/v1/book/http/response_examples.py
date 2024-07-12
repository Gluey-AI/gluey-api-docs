from app.api.v1.book.models.api.collection import CarrierSuggestions, CollectionResponse, CarrierCollectionDate, CarrierCollectionDateTime, CarrierCollectionTimeWindow, CollectionStatus, BookingResponse
from app.api.v1.common.http_responses.payloads import http_502_response
from app.api.v1.common.utils import generate_uuid, generate_short_uuid, generate_custom_uuid

dates_only_example = CollectionResponse(
    collection_id=generate_uuid(),
    collection_status=CollectionStatus.PENDING,
    uuid_ref=generate_short_uuid(6),
    carrier_collection_id=generate_custom_uuid(8),
    carrier_suggestions=CarrierSuggestions(
        collection_dates=[
            CarrierCollectionDate(
                time_id=generate_uuid(),
                date="2022-01-01",
            ),
            CarrierCollectionDate(
                time_id=generate_uuid(),
                date="2022-01-02",
            ),
            CarrierCollectionDate(
                time_id=generate_uuid(),
                date="2022-01-03",
                cost=5.0,
                cost_currency="USD"
            )
        ],
        collection_datetimes=None,
        collection_time_windows=None
    )
)

datestimes_example = CollectionResponse(
    collection_id=generate_uuid(),
    collection_status=CollectionStatus.PENDING,
    uuid_ref=generate_short_uuid(6),
    carrier_collection_id=generate_custom_uuid(8),
    carrier_suggestions=CarrierSuggestions(
        collection_dates=None,
        collection_datetimes=[
            CarrierCollectionDateTime(
                time_id=generate_uuid(),
                time="2024-07-12T09:00:00-04:00"
            ),
            CarrierCollectionDateTime(
                time_id=generate_uuid(),
                time="2024-07-12T14:30:00-04:00"
            ),
            CarrierCollectionDateTime(
                time_id=generate_uuid(),
                time="2024-07-13T09:00:00-04:00",
                cost=3.45,
                cost_currency="EUR"
            ),
            CarrierCollectionDateTime(
                time_id=generate_uuid(),
                time="2024-07-13T14:30:00-04:00",
                cost=3.45,
                cost_currency="EUR"
            )
        ],
        collection_time_windows=None
    )
)

time_windows_example = CollectionResponse(
    collection_status=CollectionStatus.PENDING,
    collection_id=generate_uuid(),
    uuid_ref=generate_short_uuid(6),
    carrier_collection_id=generate_custom_uuid(8),
    carrier_suggestions=CarrierSuggestions(
        collection_dates=None,
        collection_datetimes=None,
        collection_time_windows=[
            CarrierCollectionTimeWindow(
                time_id=generate_uuid(),
                start="2024-07-12T09:00:00-04:00",
                end="2024-07-12T12:00:00-04:00",
                cost=3.45,
                cost_currency="CHF"
            ),
            CarrierCollectionTimeWindow(
                time_id=generate_uuid(),
                start="2024-07-12T14:30:00-04:00",
                end="2024-07-12T17:30:00-04:00",
                cost=3.45,
                cost_currency="CHF"
            ),
            CarrierCollectionTimeWindow(
                time_id=generate_uuid(),
                start="2024-07-13T09:00:00-04:00",
                end="2024-07-13T12:00:00-04:00"
            ),
            CarrierCollectionTimeWindow(
                time_id=generate_uuid(),
                start="2024-07-13T14:30:00-04:00",
                end="2024-07-13T17:30:00-04:00"
            )
        ]
    )
)

booking_success_example = BookingResponse(
    collection_status=CollectionStatus.BOOKED,
    carrier_collection_id=generate_custom_uuid(8),
    paymentUrl="https://checkout.stripe.com/pay/123e4567-e89b-12d3-a456-426614174000?amount=53.50&currency=USD",
)

booking_success_example_no_payment = BookingResponse(
    collection_status=CollectionStatus.BOOKED,
    carrier_collection_id=generate_custom_uuid(8),
    paymentUrl=None,
)

collection_response_examples = {
    "dates_only": {
        "summary": "Collection Response - Dates only",
        "description": "Example response when the carrier only supports collection dates without any time interval.",
        "value": dates_only_example.model_dump()
    },
    "datetimes": {
        "summary": "Collection Response - Datetimes",
        "description": "Example response when the carrier supports collection dates with specific times.",
        "value": datestimes_example.model_dump()
    },
    "time_windows": {
        "summary": "Collection Response - Time Windows",
        "description": "Example response when the carrier supports collection dates with time windows during the day.",
        "value": time_windows_example.model_dump()
    }
}

booking_response_examples = {
    "success": {
        "summary": "Booking Response - Success",
        "description": "Example response when the booking of a collection was successful but customer still has a pending payment with the carrier.",
        "value": booking_success_example.model_dump()
    },
    "success_no_payment": {
        "summary": "Booking Response - Success - No Payment",
        "description": "Example response when the booking of a collection was successful, and no further payment is required.",
        "value": booking_success_example_no_payment.model_dump()
    }
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

http_responses_booking = {
    201: {
        "description": "Booking of collection was successful",
        "content": {
            "application/json": {
                "examples": booking_response_examples
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