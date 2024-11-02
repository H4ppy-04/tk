"""src/scripts/parser.py"""

import argparse
import sys
from typing import NoReturn

from logger import init_logger


class Parser:
    """Interface for argparse"""

    def __init__(self):
        """Constructor for `Parser`"""
        self.parser = argparse.ArgumentParser(
            description="A task manager utility",
            epilog="Author: Joshua Rose",
        )

        self.logger = init_logger(__name__)
        self.add_arguments()

    def add_arguments(self, *args, **kwargs) -> None:
        """Add arguments to `self.parser`

        :*args: TODO
        :**kwargs: TODO
        :returns: None

        """
        self.parser.add_argument(
            "--verbose",
            action="store_true",
            help="Display additional output information",
        )
        self.parser.add_argument(
            "--version",
            action="store_true",
            help="Display version information",
        )

        self.parser.add_argument(
            "--license",
            action="store_true",
            help="Display license information",
        )

        self.parser.add_argument(
            "--init",
            action="store_true",
            help="Initialize task file. WARNING: This will overwrite existing task data!",
        )

    def parse(self):
        """Wrapper for `argparse.ArgumentParser(...).parse_args()`

        :returns: TODO

        """
        return self.parser.parse_args()

    def print_help(self) -> NoReturn:
        """Wrapper for `argparse.ArgumentParser(...).print_help()`

        :returns: TODO

        """
        self.parser.print_help()
        sys.exit()
