from typing import Optional
from pydantic import BaseModel

class ProjectConfig(BaseModel):
    """Project configuration"""
    name: str
    process: Optional[str]
    description: Optional[str]
