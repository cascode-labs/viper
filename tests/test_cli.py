from unittest.mock import patch
import os
import viper
from viper.cli import cli
from viper.docs import docs_url



def test_cli_version(cli_runner):
  result = cli_runner.invoke(cli, ['--version'])
  assert result.exit_code == 0
  assert result.output == f"{viper.__version__}\n"

def test_cli_help(cli_runner):
  result = cli_runner.invoke(cli, ['--help'])
  assert result.exit_code == 0
  assert "Viper open circuit design environment" in result.output

def test_cli_welcome(cli_runner):
  result = cli_runner.invoke(cli, ['welcome'])
  assert result.exit_code == 0
  assert 'Viper open circuit design environment' in result.output
  assert f"v{viper.__version__}" in result.output

def test_cli_docs(cli_runner):
  with patch('subprocess.run') as mock_run:
      result = cli_runner.invoke(cli, ['docs'])
      assert "opening" in result.output
      mock_run.assert_called_once()
      mock_run.assert_called_with(["firefox", docs_url()],env=os.environ)

def test_cli_documentation(cli_runner):
  with patch('subprocess.run') as mock_run:
      result = cli_runner.invoke(cli, ['documentation'])
      assert result.exit_code == 0
      assert "opening" in result.output
      mock_run.assert_called_once()
      mock_run.assert_called_with(["firefox", docs_url()],env=os.environ)
