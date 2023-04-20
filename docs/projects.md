# Projects

Viper projects organize the development of a related set of circuits, most
commonly for a specific chip tape-out or a set of standard IP.  They allow the
configuration of a project work area to be declared in a `project.toml`
configuration file.  Then some of this configuration is made available as
environment variables.

Advantage:

- multi-process: Each project can support multiple libraries with each library
  defining its own process
- declarative configuration: the project configuration is defined in a
  pyproject.toml or viper.toml file located in the root folder of the 
  project repo.

## Directory Structure

Each project is created in a folder named after the project in the project
root directory.  This is set using the "default_project_root" setting and 
defaults to the parent directory of the project.  

### Example Directory tree

An example directory structure for a "bandgaps" project:

```bash
bandgaps
├── bandgap_sky130_01     # A library in the Skywater sky130 process
│   ├── controller
│   │   ├── **/*.css
│   ├── views
│   ├── model
│   ├── index.js
├── bandgap_mcu180_01    # A library in the GF MCU180 process
│   ├── css
│   │   ├── **/*.css
│   ├── images
│   ├── js
│   ├── index.html
├── pyproject.toml
└── .gitignore
```

## Project Configuration

The project's configuration is defined in a "pyproject.toml" or "viper.toml" in
the root directory of the repo.

### Example Config File

This example is for the same bandgap project.

``` toml
--8<-- "docs/pyproject.toml:2"
```

