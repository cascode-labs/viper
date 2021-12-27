#!/usr/bin/env python3
"""
Utilities for handling the viper conda environment
"""
import os
import shutil
import sys
import subprocess
from typing import List, Union
from conda.cli.python_api import Commands, run_command
from conda_build.api import get_output_file_paths, check, update_index
from conda_build.api import build as conda_build

CHANNEL_DIR_DEFAULT = "/prj/ids/ids-conda/channels/ids-skyworks"


def build(recipe_dir="./conda-recipe", channel=CHANNEL_DIR_DEFAULT):
    """Packages an IDS project into a conda package and then adds it to the main IDS conda channel."""
    if not os.path.exists(recipe_dir):
        print("ERROR: Recipe DOES NOT exist at:\n   %s", recipe_dir)
        raise FileNotFoundError
    else:
        print(f"Releasing from:\n   {recipe_dir}")

    if check(recipe_dir):
        output_files = get_output_file_paths(recipe_dir)
        print(f"Releasing the following packages:\n   {output_files}")
    else:
        print("Error: Checks Failed")
        raise Exception
    conda_build(recipe_dir)

    for file_path in output_files:
        if not os.path.exists(file_path):
            print("Error: Did not release %s", file_path)
        else:
            shutil.copy(file_path, os.path.join(channel, "linux-64"))
            update_index(channel)
            print(f"Updated the conda channel at:\n   {channel}")


def update_env(env_prefix: os.PathLike, env_yml_path: os.PathLike) -> bool:
    """ Update or create a conda environment

    Args:
        env_prefix: The prefix of the env to be updated.
            If the env doesn't exist, it is created at the prefix.
        env_yml_path: The path to the `environment.yml file <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file>`_
            defining the environment

    Returns:
        True for success, False otherwise.
    """
    pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        build()
    elif len(sys.argv) == 2:
        build(sys.argv[2])
    else:
        print("Please provide up to one argument, the conda recipe to build")
