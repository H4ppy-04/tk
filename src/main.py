#!/usr/bin/env python3
import sys

from logger import init_logger
from scripts import Parser
from scripts.commands import get_license, get_task_file, get_version, init
from task import Task


def main():
    parser = Parser()

    if len(sys.argv) <= 1:
        parser.print_help()  # exits

    args = parser.parse()
    logger = init_logger(__name__, debug=args.verbose)
    Task.logger = logger

    if args.version:
        get_version(logger)
        return

    elif args.init:
        init(logger)
        return

    elif args.license:
        get_license(logger)
        return

    elif args.name:
        task_file = get_task_file(logger)
        if task_file is None:
            logger.critical(
                "Run `python src/main.py --initialize` or specify a custom --datafile"
            )

        logger.debug(
            f"""
                     name: {args.name}
                     desc: {args.description}
                     due:  {args.due}
                     log:  {logger}
                     host: {args.host}
                     """
        )

        task = Task(
            name=args.name, description=args.description, host=args.host, due=args.due
        )
        task.write_to_file(task_file)


if __name__ == "__main__":
    main()
