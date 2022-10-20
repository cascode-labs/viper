from viper.config import config


def test_config_read():
    config_dict = config.dict()
    assert config_dict["docs"]["viper"] == "http://www.cascode-labs.org/viper/"
    assert config_dict["docs"]["viper-forge"] == \
        "https://www.cascode-labs.org/viper-forge/"
