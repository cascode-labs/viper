from click.testing import CliRunner
from viper.cli import open_project_cli

def test_project_start_cli_help():
    runner = CliRunner()
    result = runner.invoke(open_project_cli, ['--help'])
    assert result.exit_code == 0
    assert "Starts a Viper circuit design project" in result.output
