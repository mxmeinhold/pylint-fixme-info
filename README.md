[![Python CI](https://github.com/mxmeinhold/pylint-fixme-info/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mxmeinhold/pylint-fixme-info/actions/workflows/python-ci.yml)
# Pylint fixme info
A pylint plugin that emits info rather than warning for FIXME, TODO, and the like.

## Usage
To use this plugin, either run pylint with `--load-plugins=pylint_fixme_info --disable=fixme`, or add the following to your pylintrc
```toml
[MASTER]
load-plugins = pylint_fixme_info

[MESSAGES CONTROL]
disable = fixme
```

## Configuration
The following options are supported:
```
notes-info: List of note tags to take in consideration, separated by a comma. Default: FIXME,XXX,TODO
notes-info-rgx: Regular expression of note tags to take in consideration.
```
