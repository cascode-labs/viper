"""
Start project (sp)
"""
import os
# import importlib.util
import click
import subprocess

SHELL_OPTIONS = ['tcsh', 'sh', 'bash']
# ROOT_DEFAULT = "/prj"


def default_shell():
    """selects the default shell for sp"""
    login_shell = os.path.basename(os.environ["SHELL"])
    if login_shell in SHELL_OPTIONS:
        default = login_shell
    elif os.environ["VIRT_SP_SHELL_DEFAULT"] is not None:
        default = os.environ["VIRT_SP_SHELL_DEFAULT"]
    else:
        default = "tcsh"
    return default


def start_project(project, dev=False, name=None, prefix=False, shell=None, init=None, skill=None):
    """
    Start project ("sp" command)

    :param project: The name of the project to open
    :param dev: A flag for toggling the development mode
    :param name: Conda name to activate. prefix and name are mutually exclusive options.
    :param prefix: Conda Prefix to activate. prefix and name are mutually exclusive options.
    :param shell: The type of shell script specified with the --init or -i options
    :param init: Paths to one or more shell initialization scripts which will be sourced, each delimited by a ":",
                 this option can also be specified multiple times to add additional scripts.
    :param skill: Paths to one or more SKILL initialization scripts which will be loaded using loadi,
                   each delimited by a \":\", this option can also be specified multiple times to add
                   additional scripts.
    :return:
    """

    # Execute python initialization scripts
    # for idx, path in enumerate(pyinit.split(":")):
    #     if os.path.exists(path)
    #         spec = importlib.util.spec_from_file_location("init_script_module_" + str(idx), path)
    #         module = importlib.util.module_from_spec(spec)
    #         spec.loader.exec_module(module)
    #         # Seems like I'll need to hanle the case where this is ran a second time.
    #         $ I'd need to change the idx to start after the existing number.

    # Set dev env variable when dev is set
    if dev:
        os.environ["VIRT_DEV"] = "TRUE"

    # Parse shell and skill script initialization paths
    def process_file_paths(scripts):
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

    init = process_file_paths(init)

    skill = process_file_paths(skill)
    if skill is not None:
        os.environ["VIRT_SP_SKILL_INIT"] = skill

    if shell is None:
        shell = default_shell()

    commands = {
        "tcsh": "tsp",
        "sh":   "ssp",
        "bash": "ssp",
    }
    # Run command
    subprocess.run([commands[shell], str(project), str(name), str(prefix), init], env=os.environ)


##########################
# Command Line Interface #
##########################
@click.command()
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
# @click.option("--root", "-r", default=ROOT_DEFAULT, type=click.Path(exists=True, file_okay=False, dir_okay=True,
#                                                               allow_dash=False, readable=True),
#               help="Path to the project root directory containing all projects.  Defaults to \"/prj\"")
# @click.option("--pyinit", "--py", "-y", default=None, type=str,
#               help="Paths to one or more shell initialization scripts which will be sourced, each delimited by a :")
@click.option("--skill", "-k", "-replay", default=None, type=str, multiple=True,
              help="Paths to one or more SKILL initialization scripts which will be loaded using loadi, "
                   "each delimited by a \":\", this option can also be specified multiple times to add "
                   "additional scripts.")
@click.version_option()
@click.argument("project", type=str)
def sp(project, dev, name, prefix, shell, init, skill):
    """
    Start Project
     sp [options] project
     starts the given Cadence Virtuoso project
    """
    start_project(project, dev, name, prefix, shell, init, skill)


if __name__ == '__main__':
    sp(auto_envvar_prefix='VIRT')
