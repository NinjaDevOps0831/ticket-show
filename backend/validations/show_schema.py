# Make JSON Schema for validate
schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'maxLength': 20
        },
        'rate': {
            'type': 'number',
            'minimum': 0
        },
        'tags': {
            'type': 'string',
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