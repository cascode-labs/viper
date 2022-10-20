from click.testing import CliRunner
from viper.project.start import start

def test_project_start_cli_help():
    runner = CliRunner()
    result = runner.invoke(start, ['--help'])
    assert result.exit_code == 0
    assert "Starts a Viper circuit design project" in result.output
