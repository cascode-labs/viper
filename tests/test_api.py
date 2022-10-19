import os
from pathlib import Path
from pytest import fixture
from viper.api import read_config

@fixture
def set_config_path():
    os.environ["IDS_CONFIG_PATH"] = "viper.toml"

def test_read_config_viper_docs_url(set_config_path):
    assert read_config("docs", "viper") == "http://www.cascode-labs.org/viper/"
