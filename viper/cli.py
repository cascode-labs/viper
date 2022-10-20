"""
Command line interface for viper
"""
import click

from rich.panel import Panel
from rich.padding import Padding

import viper
from viper.docs import docs_url, open_docs_in_firefox
from viper.console import console
from viper.project.cli import project
from viper.project.start import start
from viper.config.cli import config_cli

@click.group()
@click.version_option(viper.__version__, '-v', '--version', message="%(version)s")
def cli():
    """Viper open circuit design environment

    Documentation: https://www.cascode-labs.org/viper/
    """

cli.add_command(config_cli)
cli.add_command(project)
cli.add_command(start)

@cli.command()
def docs():
    """Open the documentation in firefox"""
    open_docs()

@cli.command()
def documentation():
    """Open the documentation in firefox"""
    open_docs()

def open_docs():
    console.print("opening " + docs_url())
    open_docs_in_firefox()

@cli.command()
def welcome()-> None:
    """Display the Viper welcome message"""
    version = viper.__version__
    title = Padding(f"Viper open circuit design environment\nv{version}", (1,5))
    console.print("")
    console.print(Panel.fit(title, border_style="bold green"),
                  justify ="center")
    console.print(docs_url(), justify ="center")
    console.print("")

if __name__ == '__main__':
    cli(auto_envvar_prefix='VIPER')
