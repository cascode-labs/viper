import click
from viper.console import console

@click.group()
def project():
    """Interact with a project"""
    pass

@project.command()
def info():
    console.print("Project")
