from enum import Enum

class UpdateType(str, Enum):
    """Enum representing the type of update that have been made to the shipment."""

    LABELS = 'labels'
    """The labels for all parcels in the shipment has been generated and is now part of this update."""

    MANIFEST = 'manifest'
    """The shipment has been manifested with the carrier and this update might contain documents related to the manifest."""

    LOCKER_PIN = 'locker_pin'
    """A parcel locker pin code has been generated for the shipment."""

    QR_CODE = 'qr_code'
    """A QR code has been generated for the shipment. Typically for paperless services."""