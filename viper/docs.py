"""
Documentation functions
"""
import subprocess
import os
from viper.api import read_config

def docs_url() -> str:
    return read_config("docs", "viper")

def open_docs_in_firefox():
    """
    Opens the documentation in firefox
    :return:
    """
    subprocess.run(["firefox", docs_url()], env=os.environ)


if __name__ == "__main__":
    open_docs_in_firefox()
