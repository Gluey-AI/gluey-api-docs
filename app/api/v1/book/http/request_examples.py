from app.api.v1.book.models.api.collection import CollectionRequest, CollectionInfo, CollectionContact
from app.api.v1.common.utils import generate_uuid, generate_short_uuid, generate_custom_uuid

info = CollectionInfo(
    contact=CollectionContact(
        name="John Doe",
        phone="+1234567890"
    ),
    reference=generate_custom_uuid(8),
    notes_to_carrier="Unless gates are open, please dial 2* to be connected to my flat.",
    bring_label=True
)

request_collection_times = CollectionRequest(
    uuid_ref=generate_short_uuid(6),
    info=info,
    collection_dates=[
        "2022-01-01",
        "2022-01-02",
        "2022-01-03"
    ]
)

request_collection_times_no_uuid = CollectionRequest(
    uuid_ref=None,
    info=info,
    collection_dates=[
        "2022-01-01",
        "2022-01-02",
        "2022-01-03"
    ]
)

collection_request_examples = {
    "uuid": {
        "summary": "Request Collection Dates - Including your own optional UUID",
        "description": "Requesting collection dates for a shipment with your own optional UUID.",
        "value": request_collection_times.model_dump()
    },
    "no_uuid": {
        "summary": "Request Collection Dates - No UUID",
        "description": "Requesting collection dates for a shipment without your own UUID.",
        "value": request_collection_times_no_uuid.model_dump()
    },
}