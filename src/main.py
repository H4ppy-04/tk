#!/usr/bin/env python3

import argparse
import logging
import sys

from logger import init_logger
from scripts import Parser
from scripts.commands import get_version, init


def main():
    parser = Parser()

    if len(sys.argv) <= 1:
        parser.print_help()  # exits

    args = parser.parse()
    logger = init_logger(__name__, debug=args.verbose)

    if args.version:
        get_version(logger)

    if args.init:
        init(logger)


if __name__ == "__main__":
    main()
