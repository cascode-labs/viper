import types
from importlib.resources import read_text
import viper

def get_version(module: types.ModuleType) -> str:
    version_str = read_text(module,"version")
    return version_str.strip()

__version__ = get_version(viper)
