from click.testing import CliRunner
from viper.sp import sp

def test_sp_cli_help():
    runner = CliRunner()
    result = runner.invoke(sp, ['--help'])
    assert result.exit_code == 0
    assert "Start Project" in result.output


def test_sp_cli_help():
    runner = CliRunner()
    result = runner.invoke(sp, ['--version'])
    assert result.exit_code == 0
    assert "version" in result.output
