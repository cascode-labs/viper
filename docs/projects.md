# Projects

Viper projects organize the development of a related set of circuits, most
commonly for a specific chip tape-out or a set of standard IP.  They allow the
configuration of a project work area to be declared in a `project.toml`
configuration file.  Then some of this configuration is made available as
environment variables.

## Directory Structure

Each project is created in a folder named after the project in the project
root directory.  This is set using the "default_project_root" setting.  
Projects have a standard directory structure that allows multiple users to
work on a project with their own work area.
