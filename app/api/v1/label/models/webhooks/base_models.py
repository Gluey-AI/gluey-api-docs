from enum import Enum

class UpdateType(str, Enum):
    LABELS = 'labels'
    MANIFEST = 'manifest'
    LOCKER_PIN = 'locker_pin'
    QR_CODE = 'qr_code'
    OTHER = 'other'

update_type_descriptions = {
    UpdateType.LABELS: "The labels for all parcels in the shipment have been generated and are included as part of this update.",
    UpdateType.MANIFEST: "The shipment has been manifested with the carrier and this update might contain documents related to the manifest.",
    UpdateType.LOCKER_PIN: "A parcel locker pin code has been generated for the shipment.",
    UpdateType.QR_CODE: "A QR code has been generated for the shipment. Typically for paperless services.",
    UpdateType.OTHER: "An update type that is not covered by the other types."
}
