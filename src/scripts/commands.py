"""src/scripts/commands.py"""

import os
from typing import Optional


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
