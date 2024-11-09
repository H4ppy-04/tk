import dataclasses
import datetime
import json
import logging
import os
import socket
from dataclasses import InitVar, dataclass, field
from pathlib import Path
from typing import ClassVar, Optional

import dateutil


@dataclass
class Task:
    name: str
    due: Optional[dateutil.parser._parser.text_type]
    description: Optional[str] = None
    host: Optional[str] = None
    logger: ClassVar[logging.Logger]

    def __post_init__(self) -> None:
        if self.due is not None:
            try:
                now = datetime.datetime.now()
                parsed_date = dateutil.parser.parse(self.due, default=now)
                self.due = parsed_date
            except dateutil.parser.ParserError as err:
                self.logger.critical(f"Unable to parse date: {err}")

        if self.host is None:
            self.host = socket.gethostname()
            self.logger.debug(self.host)

    def due(self) -> Optional[datetime.timedelta]:
        now = datetime.datetime.now()
        if self.has_due() and self.due > now:
            return self.due - now

    def has_host(self) -> bool:
        return self.host is not None

    def has_due(self) -> bool:
        return self.due is not None

    def encode(self, task_id: int) -> dict:
        """encode task data to a format that is json-readable"""
        identifier = f"task_{task_id}"
        data = {}
        data[identifier] = {}
        data[identifier] = {
            "name": self.name,
            "description": self.description,
            "created": datetime.datetime.now().timestamp(),
            "due": str(self.due),
            "host": self.host,
            "version": "0.1.0-dev-pre",
        }
        return data

    def write_to_file(self, file):
        """Write task to file."""
        if file is None:
            return
        data = self.load_from_file(file)
        if data is None:
            self.logger.critical(
                "Couldn't parse tasks in task file. Is the file a json file?"
            )

        key = len(data.keys())
        encoded = self.encode(task_id=key)
        with open(file, "w") as fd:
            json.dump(encoded, fd, indent=4)

    def load_from_file(self, file: str | Path) -> Optional[dict]:
        """Load task data from file

        :file: TODO
        :returns: TODO

        """
        self.logger.debug(f"Attempting to load file data from {file}")

        if isinstance(file, str):
            if os.path.exists(file) is not True:
                self.logger.critical(
                    f"Failed to load file data from {file}: Path does not exist"
                )
            elif os.path.isfile(file) is not True:
                self.logger.critical(
                    f"Failed to load file data from {file}: Expected file (found directory)"
                )
            else:
                with open(os.path.join(file)) as fd:
                    return json.load(fd)

        elif isinstance(file, Path):
            if file.exists() is not True:
                self.logger.critical(
                    f"Failed to load file data from {file.name}: Path does not exist"
                )
            elif file.isfile() is not True:
                self.logger.critical(
                    f"Failed to load file data from {file.name}: Expected file (found directory)"
                )
            else:
                with open(os.path.join(file.name)) as fd:
                    return json.load(fd)
        else:
            raise TypeError
