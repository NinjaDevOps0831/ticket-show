# Make JSON Schema for validate
schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 20
        },
        'rate': {
            'type': 'number',
            'minimum': 0,
            'maximum': 10
        },
        'tags': {
            'type': 'string',
            'minLength': 1,
            'maxLength': 128
        },
        'price': {
            'type': 'number',
            'minimum': 0
        },
        'theatre_id': {
            'type': 'integer'
        }
    },
    'required': ['name', 'rate', 'tags', 'price', 'theatre_id']
}