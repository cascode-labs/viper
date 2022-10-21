# pylint: disable=C0114
from pathlib import Path
from typing import Any
import toml
from viper.config import config

def read_config(*params, toml_format=False) -> Any:
    value = config.dict()
    for param in params:
        value = value[param]
    if not isinstance(value, dict) and len(params)>0:
        if isinstance(value, Path):
            value = str(value)
        value = {param: value}
    if toml_format:
        value = toml.dumps(value)
    return value
