"""src/scripts/commands.py"""

import os
import socket
import urllib.request
from typing import Optional

from setuptools_scm import get_version as scm_version


def get_license(logger) -> None:
    """Reads local LICENSE file.

    As a fallback, reads the online file.

    :logger: TODO
    :returns: TODO

    """

    def is_connected() -> bool:
        """test internet connection"""
        try:
            socket.setdefaulttimeout(3)
            with socket.create_connection(("8.8.8.8", 53)):
                return True
        except (socket.timeout, socket.error):
            pass
        return False

    if os.path.exists("LICENSE"):
        with open("LICENSE") as fd:
            print(fd.read())
    elif is_connected():
        with urllib.request.urlopen(
            "https://raw.githubusercontent.com/H4ppy-04/tk/refs/heads/main/LICENSE"
        ) as response:
            print(response.read().decode("utf-8"))
    else:
        logger.error("Could not read license")


def get_version(logger):
    """TODO: Docstring for get_version.
    :returns: TODO

    """
    try:
        version = scm_version(root="../..", relative_to=__file__)
        print(f"tk {version}")
    except:
        logger.error("Could not get version info.")


def init(logger) -> None:
    """Initialize task files.

    This will also overwrite existing task data.

    :returns: TODO

    """

    def get_config_directory() -> Optional[str]:
        """TODO: Docstring for get_config_directory.

        :returns: TODO

        """
        env_home = os.environ.get("HOME")
        env_user = os.environ.get("USER")

        if os.environ.get("XDG_CONFIG_DIR") is not None:
            return os.environ.get("XDG_CONFIG_DIR")
        elif env_home is not None and os.path.isdir(os.path.join(env_home, ".config")):
            if os.environ.get("HOME") is not None:
                return os.path.join(env_home, ".config")
        elif env_user is not None and os.path.isdir(
            os.path.join("/", "home", env_user, ".config")
        ):
            return os.path.join("/", "home", env_user, ".config")
        else:
            return None

    cfg = get_config_directory()
    if cfg is None:
        return None
    else:
        config_directory = os.path.join(cfg, "tk")

    if os.path.isdir(config_directory):
        for i in os.listdir(config_directory):
            file = os.path.join(config_directory, i)
            logger.debug(f"Removing {file}")
            os.remove(file)
        logger.debug(f"Removing {config_directory}")
        os.removedirs(config_directory)

    os.mkdir(config_directory)
    logger.debug(f"Created {config_directory}")

    with open(os.path.join(config_directory, "tasks.json"), "w") as fd:
        fd.write("{}\n")
        logger.debug(f"Created {fd.name}")
        fd.close()

    logger.info("Success: Initialized task files")
