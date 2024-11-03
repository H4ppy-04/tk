<h1 align="center">Task Manager</h1>

<h2 align="center">The Uncomprimising Task Manager</h2>

<p align="center">
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> "Focus on the task, not the tool."

Task is the uncomprimising task-management tool for the 21st century. Forget
interfacing with Trello boards and Google tasks. Task works right here in your
command line.

## Installation and Usage

### Installation

Currently there is no way to install _task_ as it in early-development.

### Usage

_task_ can be run by calling it directly.

```bash
tk [args ...]
```
#### Commands
|  **Command**  |            **Description**            | **Implemented** |                        **Comments**                       |
|:-------------:|:-------------------------------------:|:---------------:|-----------------------------------------------------------|
|  `--verbose`  | Display additional output information |       Yes       | See `--log-level` for specific handling                   |
|  `--version`  | Display version information           |        [Yes](https://github.com/H4ppy-04/tk/issues/2)       |                                                           |
|  `--license`  | Display license information           |       Yes       | If no LICENSE file is present, output is read from GitHub |
| `--log-level` | Set verbosity level                   |        No       |                                                           |
|    `--init`   | Initialize task file(s)               |       Yes       | This command will overwrite any existing data             |


## License

MIT
