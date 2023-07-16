[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="docs/logo/8-06.jpg" alt="Logo" width="120">
  </a>

  <h2 align="center">Viper</h2>

  <p align="center">
    A hybrid integrated circuit design environment (ICDE) with extensions for both open-source and proprietary design tools
    <br/>
    Still under development and not ready for regular usage
    <br />
    <a href="https://www.cascode-labs.org/viper/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/cascode-labs/viper/discussions">Discuss</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>

## Overview

Viper is an open integrated circuit design environment.

- supports free and proprietary design tools.
- supports a cloud native, local, and on-premise compute
- supports software-based circuit design flows in addition to traditional flows.
- CLI interface
- project management with both distributed and centralized architectures

It supports both open source tools and
[Cadence Virtuoso](https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-design.html)
with the [Virtue](http://www.cascode-labs.org/virtue/) package.  

## Environment Manager

It has a circuit design package and environment manager that makes it easy
to install packages and create additional environments so the environment can
be customized to the needs of every team and every project.

[viper-forge](http://www.cascode-labs.org/viper-forge/) is developing a set of
viper packages.

## Getting Started

Setup a new machine or site using the
[install script](https://github.com/cascode-labs/viper/releases/latest/download/install-viper-linux-x86_64.sh).

## Contributing

All development planning happens in
[GitHub issues](https://github.com/cascode-labs/viper/issues) and
[GitHub discussions](https://github.com/cascode-labs/viper/discussions).

If you see an issue of interest, first check to see if there is an existing
branch named after its issue number.  Then feel free to comment on the issue
and hopefully submit a pull request with your update.

For more general questions or if you're looking for guidance on getting
started, post in
[GitHub discussions](https://github.com/cascode-labs/viper/discussions).

## Cadence Virtuoso Support

Cadence Virtuoso is supported with the [Virtue](http://www.cascode-labs.org/virtue/) package.

## Command Line Interfaces

- sp: "start project" Opens a Viper project.
      Run "sp --help" for more details
