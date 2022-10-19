from typing import Any, Dict, Union, Optional
from pathlib import Path
from pydantic import BaseSettings, DirectoryPath, BaseModel, AnyHttpUrl, FilePath


class Conda(BaseModel):
    prefixes: Dict[str, Path]
    channels: Optional[Dict[str,Union[Path, AnyHttpUrl, str]]]

class ViperConfig(BaseSettings):
    IDS_CONFIG_PATH: FilePath
    conda: Optional[Conda]
    default_project_root: DirectoryPath
    docs: Dict[str, str]
