from pydantic import BaseModel, Field
from typing import Optional

from app.api.v1.common.models.base_models import BaseAddress, Contact, MetaData
from app.api.v1.label.models.base_models import ExportReason, Incoterm

class CustomsEntity(BaseModel):
    customs_eori: Optional[str] = Field(None, description="Economic Operators Registration and Identification number. This is a unique number assigned to economic operators (e.g. importers, exporters) by customs authorities in the European Union.")
    customs_registration_number: Optional[str] = Field(None, description="Customs registration number, other than the EORI number, e.g. in Australia the Australian Business Number (ABN).")
    vat_number: Optional[str] = Field(None, description="Value Added Tax number.")
    company_number: Optional[str] = Field(None, description="Company registration number, such as the Companies House number in the UK.")
    name: str = Field(..., description="The name of the customs entity.")
    contact: Contact = Field(..., description="The contact person at the customs entity.")
    address: BaseAddress = Field(..., description="The address of the customs entity.")

class CustomsClearance(BaseModel):
    """Class representing information about customs clearance."""
    meta_data: Optional[list[MetaData]] = Field(None, description="Optional. Meta data tags to assign to customs clearance, such as country specific requirements (GST in Australia, Windsor Framework in the UK etc.)")
    incoterm: Incoterm = Field(Incoterm.DDP, description="The incoterm for customs clearance.")
    commercial_invoice: Optional[str] = Field(None, description="The commercial invoice number for customs clearance, if applicable.")
    export_reason: Optional[ExportReason] = Field(ExportReason.SALE, description="The reason for exporting the goods. This is typically a summary of the reason for the export, e.g. 'sale', 'return for refund', 'warranty' etc.")
    cpc_code: Optional[str] = Field(None, description="CPC code indicating the customs procedures applied to goods, such as import, export, transit, temporary admission, re-export, etc.") 
    seller_of_records: Optional[CustomsEntity] = Field(None, description="The seller of records for customs clearance, if applicable.")
    exporter_of_records: Optional[CustomsEntity] = Field(None, description="The exporter of records for customs clearance, if other party than the seller of records.")
    buyer_of_records: Optional[CustomsEntity] = Field(None, description="The buyer of records for customs clearance, if applicable.")
    importer_of_records: Optional[CustomsEntity] = Field(None, description="The importer of records for customs clearance, if other party than the buyer of records.")
    customs_broker: Optional[CustomsEntity] = Field(None, description="The customs broker for customs clearance, if applicable.")