from viper.cli import cli


def test_cli_config(cli_runner):
    result = cli_runner.invoke(cli, ['config'])
    assert result.exit_code == 0
    #assert 'Viper open circuit design environment' in result.output
    #assert f"v{viper.__version__}" in result.output
