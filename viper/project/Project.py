from pathlib import Path
from typing import Optional, Any, Dict
import toml
from viper.project.ProjectConfig import ProjectConfig
from viper.config.read_config import read_config

class Project():
    def __init__(self, name: str, path: Optional[Path] = None) -> None:
        self._name: str = name
        self._path: Optional[Path] = path
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def path(self) -> Optional[Path]:
        if self._path is None:
            self._path = read_config("default_project_root") / self.name
        return self._path

    @property
    def config(self) -> ProjectConfig:
        config_path = self.path / "pyproject.toml"
        config = toml.load(config_path)
        if "project" in config.keys():
            project_config = config["project"]
        else:
            raise KeyError(
                "\"Project\" table is not in the project's pyproject.toml file")
        if "tool" in config.keys() and "viper" in config["tool"].keys() \
                      and "project" in config["tool"]["viper"].keys():
            project_config.extend(config["tool"]["viper"]["project"])

        config = ProjectConfig(**project_config)
