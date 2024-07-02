
from enum import Enum

class ParcelCondition(str, Enum):
    """The condition of the parcel at the time of the tracking event."""
    GOOD = "good"
    """The parcel is in good condition."""
    DAMAGED = "damaged"
    """The parcel is damaged."""
    UNKNOWN = "unknown"
    """The condition of the parcel is unknown / not disclosed by carrier."""

class ImageFormat(str, Enum):
    """Enum representing the format of the image."""
    PNG = 'png'
    JPEG = 'jpeg'
    PDF = 'pdf'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'
    WEBP = 'webp'
    SVG = 'svg'

class LocationType(str, Enum):
    """Enum representing the type of location."""  
    AIRPORT = 'airport'
    """The location is an airport, typically a point of transit for air shipments."""
    
    POST_OFFICE = 'post_office'
    """The location is a post office where mail and parcels are handled."""
    
    PUDO = 'pudo'
    """The location is a pick up / drop-off point for customers, which could be a convenience store, grocery store etc."""
    
    WAREHOUSE = 'warehouse'
    """The location is a warehouse where goods are stored and managed."""
    
    DISTRIBUTION_CENTER = 'distribution_center'
    """The location is a distribution center where goods are distributed to various destinations."""
    
    CUSTOMS = 'customs'
    """The location is a customs facility where shipments are inspected and cleared for international transport."""
    
    SORTING_FACILITY = 'sorting_facility'
    """The location is a sorting facility where parcels are sorted by destination. Also referred to as 'carrier hub' sometimes. """
    
    LOCAL_DEPOT = 'local_depot'
    """The location is a local depot where parcels are temporarily held before delivery."""
    
    TRANSIT_CENTER = 'transit_center'
    """The location is a transit center where parcels are transferred between different modes of transport."""
    
    CUSTOMER_ADDRESS = 'customer_address'
    """The location is the customer's address, the final delivery destination."""
    
    RETURN_CENTER = 'return_center'
    """The location is a return center where returned goods are processed."""
    
    FREIGHT_TERMINAL = 'freight_terminal'
    """The location is a freight terminal where goods are transferred between different transportation modes, typically for larger shipments."""
    
    BORDER_CHECKPOINT = 'border_checkpoint'
    """The location is a border checkpoint where parcels are inspected and cleared for crossing international borders."""
    
    REGIONAL_HUB = 'regional_hub'
    """The location is a regional hub where parcels are consolidated and distributed within a region."""
    
    DELIVERY_TRUCK = 'delivery_truck'
    """The location is on a delivery truck, indicating the parcel is currently in transit."""
    
    PARCEL_LOCKER = 'parcel_locker'
    """The location is a parcel locker where parcels can be securely stored for customer pickup."""
    
    PORT = 'port'
    """The location is a seaport where goods are transferred to or from ships."""
    
    RAIL_TERMINAL = 'rail_terminal'
    """The location is a rail terminal where goods are transferred to or from trains."""
    
    OTHER = 'other'
    """The location is not covered by the other location types."""