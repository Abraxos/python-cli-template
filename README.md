# Python CLI Template

A reference program for me to use when I am creating a command-line application with Python.

## Setup

**Setting up the virtualenv**

Install a virtualenv and virtualenvwrapper according to the instructions here:

+ https://virtualenv.pypa.io/en/stable/
+ https://virtualenvwrapper.readthedocs.io/en/latest/

Then execute:

```
mkvirtualenv --python=$(which python3) python-cli-template
```

**Installing the Package**

```
(python-cli-template) pip install -e /path/to/repo
```

The `-e` installs the package in place for development.

## Testing

**Running all the unit tests with coverage:**

```
(python-cli-template) pytest -s -vv --cov python_cli_template/test/unit --cov-report=html
```

**Running all the tests with coverage:**

```
(python-cli-template) pytest -s -vv --cov python_cli_template/test --cov-report=html
```
