DEFAULTS = {
    'label': '|',
    'label_max_length': None
}


VALIDATION_SCHEMA = {
    'class_name': {
        'type': 'string',
        'required': True,
    },
    'label': {
        'type': 'string',
        'required': True
    },
    'label_max_length': {
        'type': 'integer',
        'nullable': True,
        'default': DEFAULTS['label_max_length'],
        'min': 1
    }
}
