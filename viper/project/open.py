"""
Start a Viper circuit design project
"""
import os
import platform
import subprocess
from typing import Optional, List
import click
from viper.config import config


SHELL_OPTIONS = ['tcsh', 'bash']


def open_project(project: str, dev: bool = False,
                  name: Optional[str] = None, prefix: str=False,
                  shell: Optional[str] = None, init: Optional[str] = None):
    """
    Start project ("viper start" CLI command)

    :param project: The name of the project to open
    :param dev: A flag for toggling the development mode
    :param name: Conda environment name to activate.
                 prefix and name are mutually exclusive options.
    :param prefix: Conda prefix to activate.
                   prefix and name are mutually exclusive options.
    :param shell: The type of shell script specified with the --init or -i
                  options
    :param init: Paths to one or more shell initialization scripts which will
                 be sourced, each delimited by a ":",
                 this option can also be specified multiple times to
                 add additional scripts.
    :return:
    """

    # Setup env variables
    if dev:
        os.environ["VIPER_DEV"] = "TRUE"
    os.environ["VIPER_PROJECT_NAME"] = project

    # Parse shell and skill script initialization paths
    def process_file_paths(scripts) -> Optional[List[str]]:
        if isinstance(scripts, str):
            scripts = list(scripts)
        scripts_exist = []
        if scripts is not None:
            for script_top in scripts:
                for script_bottom in script_top.split(":"):
                    if os.path.isfile(script_bottom):
                        scripts_exist.append(script_bottom)
        if len(scripts_exist) > 0:
            scripts_out = ":".join(scripts_exist)
        else:
            scripts_out = None
        return scripts_out

    config_dict = config.dict()
    projects_root = config_dict["default_project_root"]

    init = process_file_paths(init)
    if init is not None:
        os.environ["VIPER_PROJECT_INIT_SHELL"] = init

    if prefix is None:
        prefix = config_dict["conda"]["prefixes"]["virtuoso"]
    if prefix is not None:
        os.environ["VIPER_PROJECT_CONDA_PREFIX"] = str(prefix)
    
    # skill = process_file_paths(skill)
    # if skill is not None:
    #     os.environ["VIPER_SP_SKILL_INIT"] = skill

    if shell is None:
        shell = default_shell()

    commands = {
        "tcsh": "viper_open_tcsh",
        "bash": "sp_bash",
    }
    os.environ["VIPER_PROJECT_PATH"] = f"{projects_root}/{project}"

    # Run command
    completed_process = subprocess.run(["viper_open_tcsh"],
                   env=os.environ, check=True)

    if completed_process.returncode != 0:
        print(completed_process)


def default_shell():
    """selects the default shell for sp"""
    if platform.system() == "Linux":
        login_shell = os.path.basename(os.environ["SHELL"])
        if login_shell in SHELL_OPTIONS:
            default = login_shell
        elif os.environ["VIPER_SHELL_DEFAULT"] is not None:
            default = os.environ["VIPER_SHELL_DEFAULT"]
        else:
            default = "tcsh"
    elif platform.system() == "Windows":
        default = "cmd"
    else:
        raise RuntimeError("Unsupported platform: %s", str(platform.system()))
    return default


# Command Line Interface
@click.command("open")
@click.option("--dev/--nodev", "-d/-o", default=False, is_flag=True,
    help="A flag for toggling the development mode")
@click.option("--name", "-n", default=None,
    help="Conda name to activate. prefix and name are mutually exclusive options.")
@click.option("--prefix", "-p", default=None,
    help="Conda Prefix to activate. prefix and name are mutually exclusive options.")
@click.option("--shell", "-s", default=default_shell(), type=click.Choice(SHELL_OPTIONS, case_sensitive=False),
    help="The type of shell script specified with the --init or -i options")
@click.option("--init", "-i", default=None, type=str, multiple=True,
    help="Paths to one or more shell initialization scripts which will be sourced, each delimited by a \":\","
         " this option can also be specified multiple times to add additional scripts.")
#@click.option("--command", default="virtuoso", type=str, multiple=True,
#    help="The command to start the project")
@click.argument("project", type=str)
def open_project_cli(project, dev, name, prefix, shell, init):
    """
    Opens a Viper circuit design project
    """
    open_project(project, dev, name, prefix, shell, init)
