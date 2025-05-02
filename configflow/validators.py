from pydantic import BaseModel, ValidationError
from typing import Dict, Type

def validate_config(config: dict, schema: Dict[str, Type]) -> dict:
    """Validate a config dictionary against a schema."""
    class ConfigModel(BaseModel):
        pass
    
    for key, type_ in schema.items():
        ConfigModel.__annotations__[key] = type_
    
    try:
        validated = ConfigModel(**config).dict()
        return validated
    except ValidationError as e:
        raise ValueError(f"Config validation failed: {e}")