"""
Command line interface for virt
"""
import click
from .docs import docs
from .sp import start_project


#@click.option("--shell", "-s", default="tcsh", type=click.Choice(['tcsh', 'sh'], case_sensitive=False),
#              help="The shell in which to run virtuoso, either tcsh or sh.")

@click.group()
def virt():
    """
    Cadence virtuoso command-line utilities
    """
    pass

@virt.command()
def docs():


@virt.group()
def cdslib():
    """Edit a *.cdslib file"""
    pass

@cdslib.command()
def add():
    """
    Add a library
    """
    pass

@cdslib.command()
def remove():
    """
    virt cdslib remove LIB PATH
    Remove a library
    :return:
    """
    pass

@cdslib.command()
def search():
    pass

if __name__ == '__main__':
    virt(auto_envvar_prefix='VIRT')
