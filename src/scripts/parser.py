"""src/scripts/parser.py"""

import argparse
import os
import sys
from typing import NoReturn, Optional

import dateutil

from logger import init_logger
from task import Task


class Parser:
    """Interface for argparse"""

    def __init__(self):
        """Constructor for `Parser`"""
        self.parser = argparse.ArgumentParser(
            description="A task manager utility",
            epilog="https://github.com/H4ppy-04/tk",
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
            help="display additional output information",
        )
        self.parser.add_argument(
            "--version",
            action="store_true",
            help="display version information",
        )

        self.parser.add_argument(
            "--license",
            action="store_true",
            help="display license information",
        )

        self.parser.add_argument(
            "--init",
            action="store_true",
            help="initialize task file. WARNING: This will overwrite existing task data!",
        )

        self.sp_core = self.parser.add_subparsers(
            title="commands",
            description="These are the most-used commands",
        )

        self.sp_core_add = self.sp_core.add_parser(
            "add",
            description="Add a new task",
            help="write a new task to the task file",
        )

        self.sp_core_add.add_argument(
            "--datafile",
            type=argparse.FileType("r", encoding="UTF-8"),
            help="write task data to a custom file path",
            metavar="file",
            required=False,
        )

        self.sp_core_add.add_argument(
            "name",
            type=str,
            help="the name of the task",
        )

        self.sp_core_add.add_argument(
            "description", type=str, help="a short description of the task"
        )

        self.sp_core_add.add_argument(
            "due",
            type=dateutil.parser._parser.text_type,
            help="the due date of the task. (eg 2021-10-10 15:20:59, 3weeks, 2d)",
            nargs="?",
        )

        self.sp_core_add.add_argument(
            "--host",
            type=dateutil.parser._parser.text_type,
            help="host name of the current machine (defaults to $HOST)",
            default=os.getenv("HOST"),
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
