# Make JSON Schema for validate
schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'maxLength': 20
        },
        'place': {
            'type': 'string',
            'maxLength': 20
        },
        'capacity': {
            'type': 'integer',
            'minimum': 0
        },
        'image': {
            'type': 'string'
        }
    },
    'required': ['name', 'place', 'capacity', 'image']
}