from os import environ
from pathlib import Path
from typing import Dict

import toml
import yaml
import viper
from viper.api import read_config


class ProjectBuilder():

    def __init__(self, name: str) -> None:
        self._name = name
        self._paths = dict()

    @classmethod
    def build(cls, name: str) -> 'ProjectBuilder':
        builder = cls(name)
        builder._build_directories(name)
        return builder

    def _build_directories(self, name: str) -> None:
        project_path = Path(read_config("default_project_root")) / name
        self._paths = {
            "project_path": project_path,
            "user_work": project_path / "work_libs" / environ["USER"],
        }
        for path in self._paths.values():
            path.mkdir(parents=True, exist_ok=True)

    def _build_project_config(self):
        project_config = {
            "name": self.name,
            "viper_version": viper.__version__,
        }
        project_config_path = self.paths["project_path"] / "viper_project.toml"
        with open('new_toml_file.toml', 'w') as file:
            toml.dump(project_config_path, file)
        return project_config

    def _build_conda_env_definition(self):
        """Creates a Conda environment yaml file for the project"""
        dependencies = {
            "python": "3.9",
        }
        dependencies_str= []
        for name, version in dependencies.items():
            dependencies_str.append(f"{name}={version}")
        env_yaml = {
            "name": self.name,
            "channels": [
                "conda-forge",
            ],
            "dependencies": dependencies
        }
        with open('environment.yml', 'w') as file:
            yaml.dump(env_yaml,file)

    @property
    def name(self) -> str:
        return self._name

    @property
    def paths(self) -> Dict[str, Path]:
        return self._paths
