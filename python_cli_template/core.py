import logging as log
import json
from typing import Union
from pathlib import Path
from click import echo
import click
from voluptuous import MultipleInvalid

# Local module imports
from python_cli_template.validation import CONFIG_SCHEMA

# Global logging configuration
LOG_LEVEL = {'CRITICAL': log.CRITICAL, 'ERROR': log.ERROR, 'WARNING': log.WARNING, 'INFO': log.INFO,
             'DEBUG': log.DEBUG, 'NOTSET': log.NOTSET}
log.basicConfig(format='%(levelname)s - %(module)s.%(funcName)s - [%(asctime)s]: %(message)s')


def configure_logging(log_level: str):
    log.getLogger().setLevel(LOG_LEVEL[log_level])


def load_configuration_or_die(config_path: Path):
    """Loads configuration and validates it or exits the application."""
    log.info("Loading configuration: %s", str(config_path))
    config_data = json.load(config_path.open('r'))
    try:
        CONFIG_SCHEMA(config_data)
    except MultipleInvalid as exc:
        log.critical("Cannot load config from %s: %s", str(config_path), str(exc))
        exit(2)
    log.debug("Configuration loaded successfully: %s", str(config_path))
    return config_data


@click.group()
@click.option('--debug/--no-debug', default=False)
def main(debug):
    if debug:
        configure_logging('DEBUG')
        log.debug("Logging level set to debug")


@main.command()
def hello():
    echo('Hello World!')


@main.command()
@click.option('--config-file', '-c', type=click.Path(exists=True, file_okay=True, dir_okay=False,
                                                     writable=False, readable=True,
                                                     resolve_path=True, allow_dash=True),
              default=str(Path.cwd() / 'config.json'), help="JSON-formatted configuration file, "
                                                            "defaults to config.json in the current"
                                                            "directory")
def config(config_file: Union[str, Path]):
    load_configuration_or_die(Path(config_file))
