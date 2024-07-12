

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

from app.api.v1.common.models.base_models import Contact
from app.api.v1.common.utils import get_enum_description

class UnitOfMeasurement(str, Enum):
    KG = 'kg'
    L = 'l'
    G = 'g'
    ML = 'ml'
    LB = 'lb'
    OZ = 'oz'
    MT = 'mt'
    GAL = 'gal'

unit_of_measurement_descriptions = {
    UnitOfMeasurement.KG: "Kilogram (kg)",
    UnitOfMeasurement.L: "Liter (L)",
    UnitOfMeasurement.G: "Gram (g)",
    UnitOfMeasurement.ML: "Milliliter (ml)",
    UnitOfMeasurement.LB: "Pound (lb)",
    UnitOfMeasurement.OZ: "Ounce (oz)",
    UnitOfMeasurement.MT: "Metric Ton (mt)",
    UnitOfMeasurement.GAL: "Gallon (gal)"
}


class HazardClass(str, Enum):
    CLASS1 = 'class1'
    CLASS2 = 'class2'
    CLASS3 = 'class3'
    CLASS4 = 'class4'
    CLASS5 = 'class5'
    CLASS6 = 'class6'
    CLASS7 = 'class7'
    CLASS8 = 'class8'
    CLASS9 = 'class9'

hazard_class_descriptions = {
    HazardClass.CLASS1: "Class 1: Explosives.",
    HazardClass.CLASS2: "Class 2: Gases.",
    HazardClass.CLASS3: "Class 3: Flammable liquids.",
    HazardClass.CLASS4: "Class 4: Flammable solids.",
    HazardClass.CLASS5: "Class 5: Oxidizing substances and organic peroxides.",
    HazardClass.CLASS6: "Class 6: Toxic and infectious substances.",
    HazardClass.CLASS7: "Class 7: Radioactive material.",
    HazardClass.CLASS8: "Class 8: Corrosive substances.",
    HazardClass.CLASS9: "Class 9: Miscellaneous dangerous substances and articles."
}


class Division(str, Enum):
    # Class 1 divisions
    DIV1_1 = '1.1'
    DIV1_2 = '1.2'
    DIV1_3 = '1.3'
    DIV1_4 = '1.4'
    DIV1_5 = '1.5'
    DIV1_6 = '1.6'
    
    # Class 2 divisions
    DIV2_1 = '2.1'
    DIV2_2 = '2.2'
    DIV2_3 = '2.3'

division_descriptions = {
    Division.DIV1_1: "Division 1.1: Explosives with a mass explosion hazard.",
    Division.DIV1_2: "Division 1.2: Explosives with a projection hazard.",
    Division.DIV1_3: "Division 1.3: Explosives with a fire hazard.",
    Division.DIV1_4: "Division 1.4: Explosives with no significant blast hazard.",
    Division.DIV1_5: "Division 1.5: Very insensitive explosives with a mass explosion hazard.",
    Division.DIV1_6: "Division 1.6: Extremely insensitive explosives.",
    Division.DIV2_1: "Division 2.1: Flammable gases.",
    Division.DIV2_2: "Division 2.2: Non-flammable, non-toxic gases.",
    Division.DIV2_3: "Division 2.3: Toxic gases."
}


class PackagingType(str, Enum):
    DRUM = 'drum'
    JERRY_CAN = 'jerry_can'
    BOX = 'box'
    BAG = 'bag'
    CYLINDER = 'cylinder'
    TANK = 'tank'
    IBC = 'ibc'
    PAIL = 'pail'
    BOTTLE = 'bottle'
    AEROSOL_CAN = 'aerosol_can'
    FIBERBOARD_BOX = 'fiberboard_box'
    PLASTIC_CONTAINER = 'plastic_container'
    METAL_CONTAINER = 'metal_container'
    COMPOSITE_CONTAINER = 'composite_container'
    OTHER = 'other'

packaging_type_descriptions = {
    PackagingType.DRUM: "A cylindrical container used for liquids and solids.",
    PackagingType.JERRY_CAN: "A robust liquid container with a handle.",
    PackagingType.BOX: "A standard box used for various goods.",
    PackagingType.BAG: "A flexible container used for solids.",
    PackagingType.CYLINDER: "A cylindrical container used for gases.",
    PackagingType.TANK: "A large container for storing liquids.",
    PackagingType.IBC: "An intermediate bulk container used for liquids and solids.",
    PackagingType.PAIL: "A small cylindrical container, typically with a handle.",
    PackagingType.BOTTLE: "A narrow-necked container made of glass or plastic.",
    PackagingType.AEROSOL_CAN: "A pressurized container for dispensing liquids or gases.",
    PackagingType.FIBERBOARD_BOX: "A box made of fiberboard material, often used for packaging solids.",
    PackagingType.PLASTIC_CONTAINER: "A container made of plastic, used for a variety of materials.",
    PackagingType.METAL_CONTAINER: "A container made of metal, providing strong and secure packaging.",
    PackagingType.COMPOSITE_CONTAINER: "A container made from multiple materials, offering enhanced protection.",
    PackagingType.OTHER: "Another type of packaging not listed."
}

class PackagingGroup(str, Enum):
    GROUP_I = 'group_1'
    GROUP_II = 'group_2'
    GROUP_III = 'group_3'

packaging_group_descriptions = {
    PackagingGroup.GROUP_I: "Packaging Group I: High Danger.",
    PackagingGroup.GROUP_II: "Packaging Group II: Medium Danger.",
    PackagingGroup.GROUP_III: "Packaging Group III: Low Danger."
}

class Quantity(BaseModel):
    amount: float = Field(..., description="The quantity of the dangerous goods.")
    unit_of_measurement: UnitOfMeasurement = Field(..., description=f"The unit of measurement for the quantity. It can be one of the following:\n{get_enum_description(UnitOfMeasurement, unit_of_measurement_descriptions)}")

class ItemLevelDangerousGoods(BaseModel):
    un_number: str = Field(..., description="The UN number assigned to the dangerous goods, e.g. `UN3480`")
    proper_shipping_name: str = Field(..., description="The proper shipping name of the dangerous goods, e.g. `Lithium ion batteries`")
    hazard_class: HazardClass = Field(..., description=f"The hazard class of the dangerous goods. It can be one of the following:\n{get_enum_description(HazardClass, hazard_class_descriptions)}")
    division: Optional[Division] = Field(None, description=f"The division of the dangerous goods within the hazard class. Applicable for hazard class . It can be one of the following:\n{get_enum_description(Division, division_descriptions)}")
    packaging_group: Optional[PackagingGroup] = Field(None, description=f"The packaging group of the dangerous goods. It can be one of the following:\n{get_enum_description(PackagingGroup, packaging_group_descriptions)}")
    quantity: Quantity = Field(..., description="The quantity of the dangerous goods.")
    flash_point: Optional[float] = Field(None, description="The flash point of the dangerous goods, if applicable.")

class ParcelLevelDangerousGoods(BaseModel):
    packaging_type: PackagingType = Field(PackagingType.BOX, description=f"The type of packaging for the dangerous goods. It can be one of the following:\n{get_enum_description(PackagingType, packaging_type_descriptions)}")

class ShipmentLevelDangerousGoods(BaseModel):
    handling_instructions: Optional[str] = Field(None, description="Special handling instructions for the dangerous goods.")
    emergency_contact: Optional[Contact] = Field(None, description="Emergency contact information for incidents involving the dangerous goods.")