from app.api.v1.label.models.api.collection import CollectionRequest, ServiceAvailabilityRequest,DeliveryFeature
from app.api.v1.common.utils import generate_uuid, generate_short_uuid, generate_custom_uuid

request_collection_times_ups = CollectionRequest(
    carrier_service_id="2CPR",
    collection_dates=[
        "2022-01-01",
        "2022-01-02"
    ]
)

request_collection_times = CollectionRequest(
    collection_dates=[
        "2022-01-01",
        "2022-01-02"
    ]
)

request_collection_times_ten_days = CollectionRequest(
    collection_dates=[
        "2022-01-01",
        "2022-01-02",
        "2022-01-03",
        "2022-01-04",
        "2022-01-05",
        "2022-01-06",
        "2022-01-07",
        "2022-01-08",
        "2022-01-09",
        "2022-01-10"
    ]
)

availability_request = ServiceAvailabilityRequest(
    features=[
        DeliveryFeature.ADDITIONAL_INSURANCE,
        DeliveryFeature.DANGEROUS_GOODS
    ]
)

request_collection_time_no_dates = CollectionRequest(
)

service_availability_request_examples = {
    "with_dangerous_goods": {
        "summary": "Service Availability Request - Dangerous Goods",
        "description": "Request all available carrier services for a specific shipment that supports dangerous goods and additional insurance.",
        "value": availability_request.model_dump()
    }
}

collection_request_examples = {
    "two_days": {
        "summary": "Request Collection Dates - Limit to two days",
        "description": "Limit Gluey to only check for available collection dates two (2) days in advance.",
        "value": request_collection_times.model_dump()
    },
    "two_days": {
        "summary": "Request Collection Dates - Limit to two days and Express service.",
        "description": "Only check for collection dates for the carriers `express` service.",
        "value": request_collection_times_ups.model_dump()
    },
    "no_limit": {
        "summary": "Request Collection Dates - No Limit",
        "description": "No limit on collection dates - Gluey will automatically return available collection dates for the next five (5) days.",
        "value": request_collection_time_no_dates.model_dump()
    },
    "ten_days": {
        "summary": "Request Collection Dates - Extended to ten days",
        "description": "Extend Gluey to only check for available collection dates ten (10) days in advance.",
        "value": request_collection_times_ten_days.model_dump()
    },
}