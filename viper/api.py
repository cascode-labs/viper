# pylint: disable=C0114
from typing import Any
import toml
from viper.config import config

BOOTSTRAP_OVERWRITE_DEFAULT = False

def read_config(*params, toml_format=False, path: str=None) -> Any:
    if path is not None:
        config.set_config_path(path)
    value = config.dict()
    for param in params:
        value = value[param]
    if toml_format:
        value = toml.dumps(value)
    return value
