"""
Command line interface for virt
"""
import click
from .docs import docs as docs_internal
from .cdslib import add_library, include_cdslib


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
    docs_internal()

@virt.group()
def cdslib():
    """Edit a *.cdslib file"""
    pass

@cdslib.command()
@click.argument("cds_path")
@click.argument("library_name")
@click.argument("library_path")
def add():
    """
    Add a library
    """
    add_library(cds_path,library_name,library_path)

@cdslib.command()
@click.argument("cds_path")
@click.argument("include_file_path")
@click.option('-s','--soft')
def include():
    """
    Include another cds.lib file in the current one.
    :return:
    """
    include_cdslib(cds_path,include_file_path,soft)

if __name__ == '__main__':
    virt(auto_envvar_prefix='VIRT')
