# Make JSON Schema for validate
register_schema = {
    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 20
        },
        'email': {
            'type': 'string',
            'minLength': 1,
            'format': 'email'
        },
        'password': {
            'type': 'string',
            'minLength': 6
        }
    },
    'required': ['username', 'email', 'password']
}

login_schema = {
    'type': 'object',
    'properties': {
        'username': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 20
        },
        'password': {
            'type': 'string',
            'minLength': 6
        }
    },
    'required': ['username', 'password']
}