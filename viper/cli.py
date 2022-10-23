"""
Command line interface for viper
"""
import click

from rich.panel import Panel
from rich.padding import Padding

import viper
from viper.docs import docs_url
from viper.console import console
from viper.project.cli import project
from viper.project.open import open_project
from viper.config.cli import config_cli


def docs(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    url = docs_url()
    console.print(f"[link={url}]documentation[/link]")
    ctx.exit()

@click.group()
@click.version_option(viper.__version__, '-v', '--version', message="%(version)s")
@click.option("--docs", is_flag=True, callback=docs,
              expose_value=False, is_eager=True,
              help="show the documentation URL and exit")
def cli():
    """Viper open circuit design environment

    Documentation: https://www.cascode-labs.org/viper/
    """

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


cli.add_command(config_cli)
cli.add_command(project)
cli.add_command(open_project)


if __name__ == '__main__':
    cli(auto_envvar_prefix='VIPER')
