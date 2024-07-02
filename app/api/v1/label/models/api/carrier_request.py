from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import MetaData

class CarrierInstructions(BaseModel):
    """Class representing special instructions for the carrier.
    
    NOTES! Please note that not all carriers support using instructions, and many carriers have specific additional services for this purpose (e.g. 'Call recipient before delivery').
    Please check the Gluey documentation for the carrier and carrier service you are using.
    """
    delivery_instructions: str = Field(..., description="The instruction for the carrier to take into account during the delivery, e.g. 'Leave at front door'.")
    goods_instructions: str = Field(..., description="Handling instructions for the goods, e.g. 'The blue side up'.")
    recipient_instructions: str = Field(..., description="Instructions for the recipient, e.g. 'Transfer to fridge immediately upon arrival'.")

class CarrierServiceAdditionalServiceRequest(BaseModel):
    code: str = Field(..., description="The code representing the additional service / value-added service for this carrier service, e.g. if the carrier service is 'Standard Ground' then additional services might be 'saturday_delivery', 'signature', 'age_check'.")
    additional_data: Optional[list[MetaData]] = Field(None, description="Check Gluey portal for any additional data requirement to use the value-added service, e.g. for 'insurance' this could mean key-value pairs related to insurance coverage, voluntary excess etc. If you are using carrier.gluey_carrier_profile_key these values can also be hardcoded in the portal, or you can add your own Python script to map this.")

class CarrierServiceRequest(BaseModel):
    """Class representing a service provided by a parcel carrier."""
    code: str = Field(..., description="The code representing the service provided by the carrier as found in the Gluey library of carriers. For example 'express', 'standard', 'economy'.")
    additional_services: Optional[CarrierServiceAdditionalServiceRequest] = Field(None, description="Additional services to use in conjunction with the carrier service.")

class CarrierRequestModel(BaseModel):
    """Class representing a parcel carrier implemented in Gluey."""
    code: str = Field(..., description="The gluey code of the carrier as found in the library of carriers in Gluey. For example fedex, gls_logistics.")
    service: CarrierServiceRequest = Field(..., description="The service you want to use for the carrier.")
    instructions: Optional[CarrierInstructions] = Field(None, description="Will be forwarded to carrier if they support it. Any special instructions for the carrier, e.g. 'Leave at front door', 'Blue side up'.")
    implementation_version: str = Field('v1', description="The version of the carrier implemented in Gluey, for example 'v1', 'v2'. Default is 'v1' if left unspecified.")
    gluey_carrier_profile_key: Optional[str] = Field(None, description="If you maintain contract / account specific keys for the carrier in Gluey, this is the reference to that configuration (e.g. 'GLY-12345678').")
    carrier_account_keys: Optional[list[MetaData]] = Field([], description="If you maintain contract / account specific keys for the carrier in your own system, you can send them through here as a list of key-value pairs. For example 'account_number', 'customer_id', 'client_id' etc. We will then pass this through when we call the carrier API / send the EDI.") 
