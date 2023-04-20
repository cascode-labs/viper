from typing import Dict, Union, Optional, Any
from pathlib import Path
from pydantic import (BaseSettings, DirectoryPath, BaseModel, AnyHttpUrl, 
    Extra, FilePath, Field, validator)
from viper.typing import PathLike


DEFAULT_DOCS = {
    "viper": "https://www.cascode-labs.org/viper/"
}


class Conda(BaseModel):
    """Conda environment settings"""
    prefixes: Dict[str, Path]
    channels: Optional[Dict[str,Union[Path, AnyHttpUrl, str]]]

class ViperConfig(BaseSettings, extra=Extra.ignore):
    """Viper configuration settings"""
    VIPER_CONFIG_PATH: FilePath = \
        Field(description="Path to the viper config file")
    conda: Optional[Conda] = \
        Field(description="Conda environment configuration")
    default_project_root: Optional[DirectoryPath] = \
        Field(description="Default directory to place new projects")
    docs: Dict[str, str] = \
        Field(description="URLs to documentation sites",
              default=DEFAULT_DOCS)
    simulation_dirpath: DirectoryPath = \
        Field(description=\
              f"Path to the directory for storing all simulation results",
              default = Path("/tmp/simulation"))

    @validator("default_project_root", always=True)
    def get_default_project_root(cls, default_project_root: str, 
                                 values: Dict[str, Any]) -> str:
        if default_project_root is None and "VIPER_CONFIG_PATH" in values:
            return values["VIPER_CONFIG_PATH"].parent.parent
        return default_project_root
