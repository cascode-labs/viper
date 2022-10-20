import click
import toml
from pathlib import Path
from rich.markup import escape
from viper.console import console
from viper.api import read_config
from viper.config import config


@click.command(name="config")
@click.argument('parameters', nargs=-1)
@click.option('-t', '--toml', 'toml_format', default=False, help="Print the result in TOML format", is_flag=True)
@click.option('-p', '--path', default=None, help="Path to the viper environment configuration toml file")
def config_cli(parameters, toml_format, path)-> None:
    """Read the Viper environment configuration"""
    if len(parameters) == 0:
        config_dict = config.dict()
        config_out = prepare_for_print(config_dict)
        if toml_format:
            config_out = toml.dumps(config_out)
            config_out = escape(config_out)
    else:
        config_out = read_config(*parameters, toml_format=toml, path=path)
    console.print(config_out)


def prepare_for_print(input_dict: dict) -> dict:
    output = {}
    for key, value in input_dict.items():
        if isinstance(value,Path):
            value = str(value)
            output[key] = value
        elif isinstance(value, dict):
            output[key] = prepare_for_print(value)
        elif value is not None:
            output[key] = value
    return output
