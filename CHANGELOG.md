# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added 

 - `--version` flag to display version
 - `--license` flag to display license
 - `--init` flag to initialize (or re-initialize) task files
 - `--verbose` flag to toggle additional output info

### Changed

 - Upgrade dependencies: zipp, setuptools
 - Migrate `setup.py` to `pyproject.toml`
 - Add dependencies to `shell.nix` to support `--version`
