"""
Documentation functions
"""
import subprocess
import os


def docs():
    """
    Opens the documentation in firefox
    :return:
    """
    subprocess.run(["firefox" "${PREFIX}/docs/skill/"], env=os.environ)


if __name__ == "__main__":
    docs()
