import click
from viper.console import console
from viper.project.ProjectBuilder import ProjectBuilder

@click.group()
def project():
    """Interact with a project"""
    pass

@project.command()
def info():
    console.print("Project")

@click.argument('name')
@project.command()
def create(name: str):
    console.print(f"Creating Project {name}")
    ProjectBuilder.build(name)
