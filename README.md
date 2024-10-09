[![flake8-test-name-CI](https://github.com/bagerard/flake8-in-file-ignores/actions/workflows/github-actions.yml/badge.svg)](https://github.com/bagerard/flake8-in-file-ignores/actions/workflows/github-actions.yml)
[![PyPI version](https://img.shields.io/pypi/v/flake8-in-file-ignores.svg)](https://pypi.org/project/flake8-in-file-ignores/)

# Flake8 plugin for in-file-ignores

An extension for [Flake8](https://pypi.python.org/pypi/flake8) that allows to specify per-file-ignores
in the actual file instead of having to specify them in the flake8 config (the built-in way).

## Installation

    pip install flake8-in-file-ignores

## Usage
    
This plugin will scan your project files and look for lines similar to the following
    
    # flake8-in-file-ignores: noqa: E731,E123


## How it works

This plugin abuse the `parse_options` feature of flake8 to update the `per-file-ignores` config at that moment.

It scans your project to find the `# flake8-in-file-ignores: noqa:` lines and updates
the existing `per-file-ignores` options. It does all that before any checks actually run.

## Error codes

This plugin uses `IFI` as error code (but it will never raise any error)


## Changes

[v0.3.0]
* Fix issue with non-utf8 first line in the files (UnicodeDecodeError) #3
* Limit the files it scans to the files processed by the flake8 invocation #5

[v0.2.x]
* Fix and pypi doc improvement

[0.0.1]
* Initial release
