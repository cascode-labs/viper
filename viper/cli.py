"""
Command line interface for viper
"""
import click
from .docs import docs as docs_internal
from .cdslib import add_library, include_cdslib


@click.group()
def viper():
    """
    Viper CLI
    """
    pass

@viper.command()
def docs():
    docs_internal()

@viper.command()
@click.argument("cds_path")
@click.argument("library_name")
@click.argument("library_path")
def add():
    """
    Add a library
    """
    add_library(cds_path, library_name, library_path)


if __name__ == '__main__':
    viper(auto_envvar_prefix='VIPER')
