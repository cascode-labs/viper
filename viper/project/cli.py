from typing import Optional
from pathlib import Path
import click
from rich.table import Table
from viper.console import console
from viper.project.Project import Project
from viper.project.ProjectBuilder import ProjectBuilder

@click.group()
def project():
    """Interact with a project"""
    pass

@project.command()
@click.argument('name', required=False)
def info(name: Optional[str] = None ):
    """Display the project's configuration"""
    if name is None:
        name = Path.cwd().name
    project = Project(name)
    table = Table(title=f"Current Project", show_header=False)
    #table.add_column("Parameter")
    #table.add_column("Value")
    table.add_row("name", project.name)
    table.add_row("path", str(project.path))
    if project.config is not None and project.config.description is not None:
        table.add_row("description", project.config.description)
    if project.config is not None and "process" in project.config.keys():
        table.add_row("config", project.config.process)
    console.print(table)

@click.argument('name')
@project.command()
def create(name: str):
    console.print(f"Creating Project {name}")
    ProjectBuilder.build(name)
