import os
from pytest import fixture, TempPathFactory
from click.testing import CliRunner


@fixture(autouse=True)
def setup_temp_config(tmp_path_factory: TempPathFactory):
    """Runs automatically before any tests run"""
    viper_root = tmp_path_factory.mktemp("viper_root")
    config_path = viper_root / "viper.toml"
    project_path = viper_root / "projects"
    project_path.mkdir()
    project_path = str(project_path)
    with open(config_path,"w") as config_file:
        config_file.writelines([
            f"default_project_root = \"{project_path}\"\n",
            "[docs]\n",
            "viper = \"http://www.cascode-labs.org/viper/\"\n",
            "viper-forge = \"https://www.cascode-labs.org/viper-forge/\"\n",
        ])

    os.environ["VIPER_CONFIG_PATH"] = str(config_path)

@fixture(scope="session")
def cli_runner():
    return CliRunner()
