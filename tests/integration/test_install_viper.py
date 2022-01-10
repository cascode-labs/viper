import pytest
import subprocess
from pathlib import Path
from pytest import TempPathFactory

@pytest.fixture(scope="session")
def install_path(tmp_path_factory: TempPathFactory) -> Path:
    install_path = tmp_path_factory.mktemp("viper_test")
    result = subprocess.run(["install-viper-linux-x86_64.sh",
                             f"{install_path}"])
    assert result.returncode == 0
    yield install_path

def test_envs_path(install_path: Path):
    envs_path = install_path / "envs"
    assert envs_path.exists()
    
def test_prjs_path(install_path: Path):
    prjs_path = install_path / "prjs"
    assert prjs_path.exists()

def test_base_env(install_path: Path):
    base_env_path = install_path / "envs" / "viper_base"
    assert base_env_path.exists()
    bin_path = base_env_path / "bin"
    assert bin_path.exists()
