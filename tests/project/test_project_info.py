import os
import tests.project
from importlib.resources import files
from pytest import FixtureRequest, MonkeyPatch
from viper.project.Project import Project
from viper.project.ProjectConfig import ProjectConfig


def test_read_config(request: FixtureRequest, monkeypatch: MonkeyPatch):
    
    project_dirpath = files(tests.project)
    monkeypatch.chdir(str(project_dirpath))
    #os.environ[""] = str(request.fspath)
    project = Project("bandgapReferenceCircuit")
    config = project.config
    assert isinstance(config, ProjectConfig)
