from pydantic import BaseModel

class ProjectConfig(BaseModel):
    """Project configuration"""
    name: str
    process: str
    description: str
