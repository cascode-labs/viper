from viper.cli import cli


def test_cli_config_only(cli_runner):
    result = cli_runner.invoke(cli, ['config'])
    assert result.exit_code == 0
    assert 'VIPER_CONFIG_PATH' in result.output

def test_cli_config_toml(cli_runner):
    result = cli_runner.invoke(cli, ['config', '--toml'])
    assert result.exit_code == 0
    assert 'VIPER_CONFIG_PATH' in result.output
    assert '[docs]' in result.output

def test_cli_config_parameter(cli_runner):
    result = cli_runner.invoke(cli, ['config', 'VIPER_CONFIG_PATH'])
    assert result.exit_code == 0
    assert 'viper.toml' in result.output

def test_cli_config_parameter(cli_runner):
    result = cli_runner.invoke(cli, ['config', 'default_project_root'])
    assert result.exit_code == 0

def test_cli_config_parameter_toml(cli_runner):
    result = cli_runner.invoke(cli, ['config', '--toml', 'VIPER_CONFIG_PATH'])
    assert result.exit_code == 0
    assert 'VIPER_CONFIG_PATH = ' in result.output
