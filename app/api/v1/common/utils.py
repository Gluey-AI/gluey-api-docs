
from enum import Enum
import random
import uuid
import string

def get_enum_description(enum: Enum, descriptions: dict) -> str:
    return "\n".join(f" - `{item.value}`: {descriptions.get(item, 'No description available.')}" for item in enum)

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_short_uuid(length: int = 8) -> str:
    return str(uuid.uuid4())[:length]

def generate_custom_uuid(length: int = 8) -> str:
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
