from viper.project.ProjectBuilder import ProjectBuilder
from viper.config.read import config

def test_build_project_directories():
    project_name = "test_project"
    builder = ProjectBuilder.build(project_name)
    config_dict = config.dict()
    expected_project_path = config_dict["default_project_root"] / project_name
    assert expected_project_path.is_dir()

    for path in builder.paths.values():
        assert path.is_dir()
