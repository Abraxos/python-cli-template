from voluptuous import MultipleInvalid
from python_cli_template.validation import CONFIG_SCHEMA
import pytest

@pytest.mark.parametrize("config_data, expected_result", [
    ({"logging": {"level": "CRITICAL"}}, True),
    ({"logging": {"level": "ERROR"}}, True),
    ({"logging": {"level": "WARNING"}}, True),
    ({"logging": {"level": "INFO"}}, True),
    ({"logging": {"level": "DEBUG"}}, True),
    ({"logging": {"level": "ERRORS"}}, False),
    ({"logging": {"levelses": "ERROR"}}, False),
    ({"loggers": {"level": "ERROR"}}, False)
])
def test_config_schema(config_data, expected_result):
    if expected_result:
        CONFIG_SCHEMA(config_data)
    else:
        try:
            CONFIG_SCHEMA(config_data)
            raise AssertionError('MultipleInvalid not raised!')
        except MultipleInvalid as exc:
            print(str(exc))
