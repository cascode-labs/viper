from typing import Dict, Union, Optional
from pathlib import Path
from pydantic import (BaseSettings, DirectoryPath, BaseModel, AnyHttpUrl, 
    Extra, FilePath, Field)
from viper.typing import PathLike

class Conda(BaseModel):
    """Conda environment settings"""
    prefixes: Dict[str, Path]
    channels: Optional[Dict[str,Union[Path, AnyHttpUrl, str]]]

class ViperConfig(BaseSettings, extra=Extra.ignore):
    """Viper configuration settings"""
    VIPER_CONFIG_PATH: FilePath
    conda: Optional[Conda]
    default_project_root: DirectoryPath = Field()
    docs: Dict[str, str]
    simulation_dirpath: DirectoryPath
