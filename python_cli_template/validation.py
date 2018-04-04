from voluptuous import Schema, Required, Any


CONFIG_SCHEMA = Schema({Required('logging'): {Required("level"): Any('CRITICAL', 'ERROR', 'WARNING',
                                                                     'INFO', 'DEBUG')}})
