
from enum import Enum

def get_enum_description(enum: Enum, descriptions: dict) -> str:
    return "\n".join(f" - `{item.value}`: {descriptions.get(item, 'No description available.')}" for item in enum)