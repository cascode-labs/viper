from viper.api import read_config


def test_read_config_viper_docs_url():
    assert read_config("docs", "viper") == "http://www.cascode-labs.org/viper/"
