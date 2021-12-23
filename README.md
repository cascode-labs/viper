[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Viper
Viper is a integrated circuit design environment.  It supports design workflows with both free open-source and proprietary commercial software tools.

It supports both open source tools and [Cadence Virtuoso](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-design.html).  

Environment Manager
-------------------
It has a circuit design package and environment manager.
It is built on top of [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) 
and supports SKILL code.  

Cadence Virtuoso Support
------------------------
- Initializes skill Code from each of the packages in a Conda environment
- Documents how to build a Conda package containing SKILL
- Provides a library of SKILL functions

Command Line Interfaces
----------------------

* sp: "start project" Opens a project in virtuoso.
      Run "sp --help" for more details
  
* virt: Virtuoso command line utilities
      Run "virt --help" for more details
