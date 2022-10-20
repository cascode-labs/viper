# pylint: disable=C0114
import os
from pathlib import Path
from os import environ
from typing import Union, Optional
import toml
from viper.config.config_data import ViperConfig

   
class Config():
    _CONFIG_PATH: Optional[Path] = None
    _CONFIG: Optional[ViperConfig] = None

    @classmethod
    def set_config_path(cls, path: Union[Path, str]) -> None:
        if isinstance(path, str):
            path = Path(path)
        cls._CONFIG_PATH = path

    @classmethod
    def reload(cls, path: Optional[Union[Path, str]]) -> None:
        if path is not None:
            cls._CONFIG_PATH = Path(path)
        cls._read_config()

    @classmethod
    def config_path(cls) -> Path:
        if cls._CONFIG_PATH is None:
            if environ.get("VIPER_CONFIG_PATH") is not None:
                cls._CONFIG_PATH = Path(environ["VIPER_CONFIG_PATH"])
            else: 
                cls._CONFIG_PATH = Path(os.getcwd()) / "viper.toml"
        return cls._CONFIG_PATH
    
    @classmethod
    def dict(cls) -> dict:
        if cls._CONFIG is None:
            cls._CONFIG = cls._read_config()
        return cls._CONFIG.dict()

    @classmethod
    def _read_config(cls) -> ViperConfig:
        config = toml.load(cls.config_path())
        config["VIPER_CONFIG_PATH"] = cls.config_path()
        config = ViperConfig(**config)
        return config

config = Config
