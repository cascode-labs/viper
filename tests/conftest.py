from pytest import fixture
from click.testing import CliRunner

@fixture(scope="session")
def cli_runner():
    return CliRunner()