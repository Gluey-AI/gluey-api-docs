
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.utils import get_enum_description

class ErrorCode(str, Enum):
    ADDRESS_POST_CODE = "address_post_code"
    ADDRESS_STATE_CODE = "address_state_code"
    ADDRESS_STREET_ADDRESS = "address_street_address"
    ADDRESS_VERIFICATION_FAILED = "address_verification_failed"
    AUTHENTICATION_FAILURE = "authentication_failure"
    AUTHORIZATION_FAILURE = "authorization_failure"
    BAD_REQUEST = "bad_request"
    CARRIER_DATA_ERROR = "carrier_data_error"
    CONTACT_MISSING = "contact_missing"
    COUNTRY_NOT_SUPPORTED = "country_not_supported"
    DATA_VALIDATION_ERROR = "data_validation_error"
    DUPLICATE_REQUEST = "duplicate_request"
    EMAIL_MISSING = "email_missing"
    INTERNAL_SERVER_ERROR = "internal_server_error"
    INVALID_TRACKING_NUMBER = "invalid_tracking_number"
    ITEMS_MISSING = "items_missing"
    ITEM_DESCRIPTION_TOO_LONG = "item_description_too_long"
    ITEM_INFO_MISSING_DESCRIPTION = "item_info_missing_description"
    ITEM_INFO_MISSING_COUNTRY_OF_ORIGIN = "item_info_missing_country_of_origin"
    ITEM_INFO_MISSING_VALUE = "item_info_missing_value"
    ITEM_INFO_MISSING_HS_CODE = "item_info_missing_hs_code"
    ITEM_INFO_MISSING_QUANTITY = "item_info_missing_quantity"
    LABEL_GENERATION_ERROR = "label_generation_error"
    LABEL_GENERATION_ERROR_GLUEY = "label_generation_error_gluey"
    META_DATA_ERROR = "meta_data_error"
    MOBILE_NUMBER_MISSING = "mobile_number_missing"
    NO_IMPLEMENTATION = "no_implementation"
    PACKAGE_SIZE_ERROR = "package_size_error"
    PACKAGE_WEIGHT_ERROR = "package_weight_error"
    PAST_BOOKING_CUTOFF_TIME = "past_booking_cutoff_time"
    PAST_CANCEL_CUTOFF_TIME = "past_cancel_cutoff_time"
    POSTCODE_NOT_SUPPORTED = "post_code_not_supported"
    SERVICE_NOT_SUPPORTED = "service_not_supported"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    TIMEOUT = "timeout"
    OTHER = "other"

error_code_descriptions = {
    ErrorCode.ADDRESS_POST_CODE: "The address post code is missing or incorrect.",
    ErrorCode.ADDRESS_STATE_CODE: "The address state code is missing or incorrect.",
    ErrorCode.ADDRESS_STREET_ADDRESS: "The street address is missing or incorrect.",
    ErrorCode.ADDRESS_VERIFICATION_FAILED: "The address data provided was incorrect or could not be verified.",
    ErrorCode.AUTHENTICATION_FAILURE: "Authentication with the Carrier API failed.",
    ErrorCode.AUTHORIZATION_FAILURE: "Authorization with the Carrier API failed.",
    ErrorCode.BAD_REQUEST: "The request to the Carrier API was malformed or incorrect.",
    ErrorCode.CARRIER_DATA_ERROR: "The carrier has provided faulty data to Gluey for local label implementation.",
    ErrorCode.CONTACT_MISSING: "The contact information is missing.",
    ErrorCode.COUNTRY_NOT_SUPPORTED: "The country is not supported by the Carrier / Service.",
    ErrorCode.DATA_VALIDATION_ERROR: "The data provided is invalid or does not meet the Carrier API's requirements.",
    ErrorCode.DUPLICATE_REQUEST: "A request with the same data has already been made.",
    ErrorCode.EMAIL_MISSING: "The email address is missing.",
    ErrorCode.INTERNAL_SERVER_ERROR: "Internal server error in the Carrier API.",
    ErrorCode.INVALID_TRACKING_NUMBER: "The tracking number provided is invalid.",
    ErrorCode.ITEMS_MISSING: "The items are missing and required by carrier.",
    ErrorCode.ITEM_DESCRIPTION_TOO_LONG: "The the description of one of the items is too long.",
    ErrorCode.ITEM_INFO_MISSING_DESCRIPTION: "The description is missing for one of the items.",
    ErrorCode.ITEM_INFO_MISSING_COUNTRY_OF_ORIGIN: "The country of origin is missing for one of the items.",
    ErrorCode.ITEM_INFO_MISSING_VALUE: "The unit value is missing for one of the items.",
    ErrorCode.ITEM_INFO_MISSING_HS_CODE: "The HS code is missing for one of the items.",
    ErrorCode.ITEM_INFO_MISSING_QUANTITY: "The quantity is missing for one of the items.",
    ErrorCode.LABEL_GENERATION_ERROR: "Error occurred while generating the label.",
    ErrorCode.LABEL_GENERATION_ERROR_GLUEY: "Error occurred while generating the label in Gluey.",
    ErrorCode.META_DATA_ERROR: "The carrier meta data provided is incorrect.",
    ErrorCode.MOBILE_NUMBER_MISSING: "The mobile number is missing.",
    ErrorCode.NO_IMPLEMENTATION: "The Carrier does not have any implementation for this operation.",
    ErrorCode.PACKAGE_SIZE_ERROR: "The package size is invalid or exceeds the carrier's limits.",
    ErrorCode.PACKAGE_WEIGHT_ERROR: "The package weight is invalid or exceeds the carrier's limits.",
    ErrorCode.PAST_BOOKING_CUTOFF_TIME: "The request to book the collection was made after the cutoff time.",
    ErrorCode.PAST_CANCEL_CUTOFF_TIME: "The request to cancel the collection was made after the cutoff time.",
    ErrorCode.POSTCODE_NOT_SUPPORTED: "The post code is not supported by the Carrier / Service.",
    ErrorCode.RATE_LIMIT_EXCEEDED: "The rate limit for the Carrier API has been exceeded.",
    ErrorCode.SERVICE_NOT_SUPPORTED: "The service is not supported by the Carrier / Service for this account.",
    ErrorCode.TIMEOUT: "The Carrier API timed out.",
    ErrorCode.OTHER: "An error occurred in the Carrier API which Gluey were note able to classify."
}

class CarrierPayload(BaseModel):
    payload_media: str = Field(..., description="The media type of the payload, e.g. `application/xml`, `application/json`")
    payload_http_status_Code: int = Field(..., description="The original HTTP status code of the payload, e.g. 200, 400, 500. `Not recommended to use`. For example, a SOAP-api might give a 200 http status code whilst still failing due to data validation errors.")
    payload_base64: str = Field(..., description="The base64 encoded payload, e.g. `9pj3wfolmucmnt7iw3r4n34ymcwp4+yctx6+94mqc3zxtc43tyew9f7hsduvknvlufhksmuygvmred748745698y09gfimcnv875mz489z`")

class GlueyErrorClassification(BaseModel):
    error_code: ErrorCode = Field(..., description=f"Glueys own error code of the issue in the Carrier API. It can be one of the following:\n{get_enum_description(ErrorCode, error_code_descriptions)}")
    error_description: str = Field(..., description="A description of the error", example="The address data provided was incorrect")
    http_status_code: int = Field(..., description="The HTTP status code of the error. NOTE! This is not carriers original one, it's Glueys harmonised status code. For example, a SOAP-api might give a 200 http status code whilst still failing due to data validation errors. This means Gluey respond with a 422 indicating the request failed due to data validation errors.", example=422)

class CarrierApiError(BaseModel):
    gluey_error_classification: GlueyErrorClassification = Field(..., description="This is Glueys own classification and description of the error that happened in the Carrier API.")
    carrier_payload: Optional[CarrierPayload] = Field(None, description="If available, depending on error. The original payload returned from the carrier API.")

error_state = CarrierApiError(
    gluey_error_classification=GlueyErrorClassification(
        error_code=ErrorCode.ADDRESS_STATE_CODE,
        error_description="The address data provided was incorrect - state code is missing or wrong.",
        http_status_code=422
    ),
    carrier_payload=CarrierPayload(
        payload_media="application/xml",
        payload_http_status_Code=200,
        payload_base64="9pj3wfolmucmnt7iw3r4n34ymcwp4+yctx6+94mqc3zxtc43tyew9f7hsduvknvlufhksmuygvmred748745698y09gfimcnv875mz489z"
    )
)

error_no_implementation = CarrierApiError(
    gluey_error_classification=GlueyErrorClassification(
        error_code=ErrorCode.NO_IMPLEMENTATION,
        error_description="Carrier API does not have any endpoint implemented for this operation.",
        http_status_code=501
    ),
    carrier_payload=None
)

error_timeout = CarrierApiError(
    gluey_error_classification=GlueyErrorClassification(
        error_code=ErrorCode.TIMEOUT,
        error_description="Carrier API timed out.",
        http_status_code=504
    ),
    carrier_payload=None
)

error_response_examples = {
    "no_implementation": {
        "summary": "Carrier API Error - No implementation",
        "description": "Example response that indicates that the carrier API does not have any endpoint implemented for this operation.",
        "value": error_no_implementation.model_dump()
    },
    "timeout": {
        "summary": "Carrier API Error - Timeout",
        "description": "Example response that indicates that the carrier API timed out.",
        "value": error_timeout.model_dump()
    },
    "state_code": {
        "summary": "Carrier API Error - Address State Code",
        "description": "Example response when the carrier's API returns an error indicating that the address state code is missing or wrong.",
        "value": error_state.model_dump()
    }
}

http_502_response = {
        "model": CarrierApiError,
        "description": "Carrier API Error",
        "content": {
            "application/json": {
                "examples": error_response_examples
            }
        }
    }