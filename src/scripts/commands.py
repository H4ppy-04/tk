"""src/scripts/commands.py"""

import os
import socket
import urllib.request
from typing import Optional


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
        return None


def get_version(logger) -> str:
    """TODO: Docstring for get_version.
    :returns: TODO

    """
    pass


def init(logger) -> None:
    """Initialize task files.

    This will also overwrite existing task data.

    :returns: TODO

    """

    def get_config_directory() -> Optional[str]:
        """TODO: Docstring for get_config_directory.

        :returns: TODO

        """
        if os.environ.get("XDG_CONFIG_DIR") is not None:
            return os.environ.get("XDG_CONFIG_DIR")
        elif os.environ.get("HOME") is not None and os.path.isdir(
            os.path.join(os.environ.get("HOME"), ".config")
        ):
            return os.path.join(os.environ.get("HOME"), ".config")
        elif os.environ.get("USER") is not None and os.path.isdir(
            os.path.join("/", "home", os.environ.get("USER"), ".config")
        ):
            return os.path.join("/", "home", os.environ.get("USER"), ".config")
        else:
            return None

    if get_config_directory() is None:
        return None
    else:
        config_directory = os.path.join(get_config_directory(), "tk")

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
