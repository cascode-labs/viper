from viper.cli import cli
from viper.config.read import config


def test_build_project_cli_directories(cli_runner):
    project_name = "test_project_cli"
    result = cli_runner.invoke(cli, ['project', "create", project_name])
    assert result.exit_code == 0
    config_dict = config.dict()
    expected_project_path = config_dict["default_project_root"] / project_name
    assert expected_project_path.is_dir()
