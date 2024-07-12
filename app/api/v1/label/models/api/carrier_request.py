from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import MetaData

class CarrierInstructions(BaseModel):
    """Class representing special instructions for the carrier.
    
    NOTES! Please note that not all carriers support using instructions, and many carriers have specific value added services for this purpose (e.g. 'Call recipient before delivery').
    Please check the Gluey documentation for the carrier and carrier service you are using.
    """
    delivery_instructions: Optional[str] = Field(None, description="The instruction for the carrier to take into account during the delivery, e.g. 'Leave at front door'.")
    goods_instructions: Optional[str] = Field(None, description="Handling instructions for the goods, e.g. 'The blue side up'.")
    recipient_instructions: Optional[str] = Field(None, description="Instructions for the recipient, e.g. 'Transfer to fridge immediately upon arrival'.")

class ValueAddingServiceRequest(BaseModel):
    id: str = Field(..., description="Glueys ID of the value adding service for a particular Carrier Service. This can typically be found in the library of carriers in Gluey is the carriers own ID of the value add, e.g. 'signature', 'age_check'.")
    additional_data: Optional[list[MetaData]] = Field(None, description="Check Gluey portal for any additional data requirement to use the value-added service, e.g. for 'insurance' this could mean key-value pairs related to insurance coverage, voluntary excess etc.")

class CarrierServiceRequest(BaseModel):
    """Class representing a service provided by a parcel carrier."""
    id: str = Field(..., description="Glueys ID of the carrier service. This can typically be found in the library of carriers in Gluey is the carriers own ID of the service, e.g. 'standard_ground', 'express', 'home_delivery'.")
    value_adding_services: Optional[list[ValueAddingServiceRequest]] = Field(None, description="Value adding services to use in conjunction with the main carrier service, i.e. for 'home_delivery' this might be value-adds such as 'cash_on_delivery', 'verification_signature', 'insurance' etc.")

class CarrierRequestModel(BaseModel):
    """Class representing a parcel carrier implemented in Gluey."""
    id: str = Field(..., description="Glueys ID that identifies the carrier in our system, e.g. 'poste_italiane', 'yodel'. The Gluey ID of the carrier as found in the library of carriers in Gluey.")
    service: CarrierServiceRequest = Field(..., description="The service you want to use for the carrier.")
    meta_data: Optional[list[MetaData]] = Field([], description="If you maintain carrier specific meta data such as API keys, OAuth keys, account numbers, client_ids in your own system you can pass these keys through here. Check in the Gluey portal for any additional configurations you can send through.") 
    instructions: Optional[CarrierInstructions] = Field(None, description="Will be forwarded to carrier if they support it. Any special instructions for the carrier, e.g. 'Leave at front door', 'Blue side up'.")
    gluey_profile: Optional[str] = Field(None, description="If you maintain carrier specific meta data such as API keys, OAuth keys, account numbers, client_ids in Gluey pass through the reference to that configuration here (e.g. 'GLY-12345678'). Since Gluey supports several different profiles it should be a unique profile you have configured in Gluey.")
