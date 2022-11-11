from typing import Optional
import click
from viper.console import console
from viper.project.Project import Project
from viper.project.ProjectBuilder import ProjectBuilder

@click.group()
def project():
    """Interact with a project"""
    pass

@project.command()
@click.argument('name')
def info(name: Optional[str] = None ):
    console.print("Project")
    project = Project(name)
    print(project.name)
    print(project.path)
    print(project.config)
    #config = project.config
    #print(config.dict())

@click.argument('name')
@project.command()
def create(name: str):
    console.print(f"Creating Project {name}")
    ProjectBuilder.build(name)
