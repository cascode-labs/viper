from viper.project.Project import Project
from viper.project.ProjectConfig import ProjectConfig
def test_read_config():
    project = Project("ids_dev")
    config = project.config
    assert isinstance(project.config, ProjectConfig)
