from datetime import datetime, timedelta, timezone

from app.api.v1.common.models.base_models import Dimensions, MetaData, TrackingLevel, UnitOfMeasurement, UnitOfWeight, Weight
from app.api.v1.tracking.models.base_models import CarrierEventCodeDetail, CarrierLocationCode, GlueyEventCodeDetail, GlueyMilestone, LocationType, ParcelCondition, TrackingEventAddress, TrackingEventCodes, TrackingEventDateTime, TrackingEventLocation, TrackingEventPhysicalData
from app.api.v1.tracking.models.webhooks.tracking_event import OtherUpdates, TrackingEvent, TrackingEventParcel, TrackingWebhookEvent

creation_date = datetime.now(timezone.utc)
adjusted_minus_five_hours = creation_date - timedelta(hours=5)
adjusted_minus_five_hours = adjusted_minus_five_hours.astimezone(timezone(timedelta(hours=1)))
adjusted_plus_four_hours = creation_date.astimezone(timezone(timedelta(hours=4)))
adjusted_plus_four_hours_one_minute = creation_date.astimezone(timezone(timedelta(hours=4, minutes=1)))

adjusted_plus_two_hours = creation_date.astimezone(timezone(timedelta(hours=2)))

adjusted_plus_nine_hours = creation_date.astimezone(timezone(timedelta(hours=9)))
adjusted_plus_five_days = creation_date + timedelta(days=5)
adjusted_plus_five_days = adjusted_plus_five_days.astimezone(timezone(timedelta(hours=1)))

shipment_level_event = [TrackingWebhookEvent(
    shipment_id="d1b82d77-526b-4a6d-a456-b97c1e34cafe",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR5"), MetaData(key="zone", value="B")],
    carrier_id="uk_carrier",
    carrier_tracking_id="JD0002234001100086",
    tracking_level=TrackingLevel.SHIPMENT,
    event=TrackingEvent(
        carrier_meta_data=[MetaData(key="grn_info", value="118045")],
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_four_hours.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.COLLECTION,
                code="collected",
                sub_code="other"
            ),
            carrier=CarrierEventCodeDetail(
                code="GC",
                freetext_detail="Collected"
            )
        ),
        location=TrackingEventLocation(
            carrier_location_coding=CarrierLocationCode(
                code="MIDDLETON SERVICE CENTRE"
            )
        ),
        other=None
    )
),
TrackingWebhookEvent(
    shipment_id="1588d329-94ab-43a3-a095-1a4fd1cbf5ce",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR4"), MetaData(key="zone", value="C")],
    carrier_id="eu_carrier",
    carrier_tracking_id="LTN19768633N1",
    tracking_level=TrackingLevel.SHIPMENT,
    event=TrackingEvent(
        carrier_meta_data=None,
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_two_hours.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.IN_TRANSIT,
                code="carrier",
                sub_code="other"
            ),
            carrier=CarrierEventCodeDetail(
                code="275",
                freetext_detail="In transit"
            )
        ),
        location=TrackingEventLocation(
            address=TrackingEventAddress(
                type=LocationType.OTHER,
                name="Pr Shop Westland Center",
                city="Anderlecht",
                postal_code="1070",
                iso_country="BE"
            )
        ),
        other=None
    )
)]

parcel_level_events = [TrackingWebhookEvent(
    shipment_id="d1b82d77-526b-4a6d-a456-b97c1e34cafe",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR5"), MetaData(key="zone", value="B")],
    carrier_id="uk_carrier",
    carrier_tracking_id="JD0002234001100999",
    tracking_level=TrackingLevel.PARCEL,
    parcel=TrackingEventParcel(
        carrier_tracking_id="JD0002234001100998",
        parcel_id="49ffe1dc-d4bb-414f-8c97-5efa20202fb6",
    ),
    event=TrackingEvent(
        carrier_meta_data=[MetaData(key="grn_info", value="118045")],
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_four_hours.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.COLLECTION,
                code="collected",
                sub_code="other"
            ),
            carrier=CarrierEventCodeDetail(
                code="GC",
                freetext_detail="Collected"
            )
        ),
        location=TrackingEventLocation(
            carrier_location_coding=CarrierLocationCode(
                code="GATESHEAD SERVICE CENTRE"
            )
        ),
        other=None
    )
),
TrackingWebhookEvent(
    shipment_id="d1b82d77-526b-4a6d-a456-b97c1e34cafe",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR5"), MetaData(key="zone", value="B")],
    carrier_id="super_carrier",
    carrier_tracking_id="JD0002234001100999",
    tracking_level=TrackingLevel.PARCEL,
    parcel=TrackingEventParcel(
        carrier_tracking_id="JD0002234001100997",
        parcel_id="a2d7cf49-4ff5-495d-9d07-bbfc69afa5dd",
    ),
    event=TrackingEvent(
        carrier_meta_data=[MetaData(key="grn_info", value="118045")],
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_four_hours_one_minute.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.COLLECTION,
                code="collected",
                sub_code="other"
            ),
            carrier=CarrierEventCodeDetail(
                code="GC",
                freetext_detail="Collected"
            )
        ),
        location=TrackingEventLocation(
            carrier_location_coding=CarrierLocationCode(
                code="GATESHEAD SERVICE CENTRE"
            )
        ),
        other=None
    )
)]

shipment_level_event_with_other = [TrackingWebhookEvent(
    shipment_id="41752ba3-08b9-4a67-8766-756136214efe",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR5"), MetaData(key="zone", value="B")],
    carrier_id="au_carrier",
    carrier_tracking_id="ABC000128B4C5",
    tracking_level=TrackingLevel.SHIPMENT,
    event=TrackingEvent(
        carrier_meta_data=None,
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_four_hours.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.COLLECTION,
                code="collected",
                sub_code="other"
            ),
            carrier=CarrierEventCodeDetail(
                code="GC",
                freetext_detail="Collected"
            )
        ),
        location=TrackingEventLocation(
            carrier_location_coding=CarrierLocationCode(
                code="SYD"
            )
        ),
        other=OtherUpdates(
            eta=adjusted_plus_five_days,
        )
    )
),
TrackingWebhookEvent(
    shipment_id="a5173dba-5dd5-4358-9a71-a73792b86898",
    shipment_uuid_ref=None,
    shipment_meta_data=[MetaData(key="hub_code", value="GWR4"), MetaData(key="zone", value="C")],
    carrier_id="middle_east_carrier",
    carrier_tracking_id="ARX98739823",
    tracking_level=TrackingLevel.SHIPMENT,
    event=TrackingEvent(
        carrier_meta_data=None,
        event_time=TrackingEventDateTime(
            created_utc=adjusted_minus_five_hours.replace(microsecond=0),
            carrier_utc=adjusted_plus_two_hours.replace(microsecond=0)
        ),
        codes=TrackingEventCodes(
            gluey=GlueyEventCodeDetail(
                milestone=GlueyMilestone.IN_TRANSIT,
                code="processed_at_carrier_facility",
                sub_code="sortation_hub"
            ),
            carrier=CarrierEventCodeDetail(
                code="SH25",
                freetext_detail="At facility"
            )
        ),
        location=TrackingEventLocation(
            address=TrackingEventAddress(
                type=LocationType.SORTING_FACILITY,
                name="Riyadh Sorting Facility",
                city="Riyadh",
                postal_code="12345",
                iso_country="SA"
            )
        ),
        other=OtherUpdates(
            carrier_weight_dims=TrackingEventPhysicalData(
                weight=Weight(
                    value=1.567,
                    unit=UnitOfWeight.LB
                ),
                dimensions=Dimensions(
                    length=45.3,
                    width=29.7,
                    height=14.8,
                    unit=UnitOfMeasurement.CM
                )
            )
        )
    )
)]

webhook_post_examples = {
    "single_parcel_shipment": {
        "summary": "Shipment Level Events",
        "description": "Tracking events - Shipment-level without association to a parcel.",
        "value": shipment_level_event
    },
    "multi_parcel_shipment": {
        "summary": "Parcel Level Events",
        "description": "Tracking events - Multi-parcel shipment where each parcel receives a tracking event.",
        "value": parcel_level_events
    },
    "other_updates": {
        "summary": "Shipment Level Events with Other Updates",
        "description": "Tracking events - Shipment-level without association to a parcel and with additional updates such as ETA and weight/dimensions from carriers sortation facility.",
        "value": shipment_level_event_with_other
    }
}