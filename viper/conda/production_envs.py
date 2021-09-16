"""
A pair of production base environments.
"""


def update_envs_production(env_dir_name, env_yml_path,
                           env_path_a="/prj/ids/ids-conda/envs_ping",
                           env_path_b="/prj/ids/ids-conda/envs_pong",
                           prod_env_path_link="/prj/ids/ids-conda/envs_prod"):
    """ Update or creates a climate of environments.

    Updates or creates a given production climate.  A production env

    """
    # Determine the current production and staging paths
    production_path = os.path.realpath(prod_env_path_link)
    if production_path == env_path_a:
        staged_path = env_path_b
        prod_path = env_path_a
    elif production_path == env_path_b:
        staged_path = env_path_a
        prod_path = env_path_a
    else:
        raise PingPongInconsistentException()

    print("Updating env %s/n "
          " Current prod: ", env_dir_name)

    # Update the conda env
    subprocess.run(["conda", "env", "update",
                    "-p", os.path.join(staged_path, env_dir_name),
                    "-f", env_yml_path])

    # Swap staged and production paths
    os.symlink(staged_path, prod_env_path_link)

    print(" Updated env %s and moved production to:\n %s", staged_path)


class PingPongInconsistentException(Exception):
    """ An exception thrown when the production env is pointing to neither
    the ping, nor pong environment.
    """
    pass