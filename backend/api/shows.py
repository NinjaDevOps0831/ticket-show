from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from jsonschema import validate

# Import db and Show model
from extensions import db
from models.shows import Show

# Import auth middleware
from middlewares.auth import admin_role_required

# Import validation JSON Schema
from validations.show_schema import schema

shows = Blueprint('shows', __name__)

@shows.route('/<show_id>', methods=['GET'])
@jwt_required()
def get_by_id(show_id):
    current_show = Show.query.get(show_id)

    show_data = {
        'id': current_show.id,
        'name': current_show.name,
        'rate': current_show.rate,
        'tags': current_show.tags,
        'price': current_show.price,
        'theatre_id': current_show.theatre_id
    }

    return jsonify(show_data), 200



# Get Router
@shows.route('/theatres/<theatre_id>', methods=['GET'])
@jwt_required()
def get_by_theatre_id(theatre_id):
    shows = Show.query.filter(Show.theatre_id == theatre_id).all()
    shows_data = [
        {
            'id': show.id,
            'name': show.name,
            'rate': show.rate,
            'tags': show.tags,
            'price': show.price,
            'theatre_id': show.theatre_id
        }
        for show in shows
    ]

    return jsonify(shows_data), 200


# Store Router
@shows.route('/', methods=['POST'])
@admin_role_required
def store():
    data = request.get_json()

    # Validate datas
    try:
        validate(instance=data, schema=schema)
    # Validate failed
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Validate Success
    name = data['name']
    rate = data['rate']
    tags = data['tags']
    price = data['price']
    theatre_id = data['theatre_id']

    show = Show(name, rate, tags, price, theatre_id)

    db.session.add(show)
    db.session.commit()

    return jsonify({ 'message': 'Show created successful' }), 201



# Update Router
@shows.route('/<show_id>', methods=['PUT'])
@admin_role_required
def update(show_id):
    data = request.get_json()


    # Validate datas
    try:
        validate(instance=data, schema=schema)
    # Validate failed
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Validate Success
    new_name = data['name']
    new_rate = data['rate']
    new_tags = data['tags']
    new_price = data['price']
    new_theatre_id = data['theatre_id']

    current_show = Show.query.get(show_id)

    if not current_show:
        return jsonify({'message': 'Show not found'}), 404
    
    current_show.name = new_name
    current_show.rate = new_rate
    current_show.tags = new_tags
    current_show.price = new_price
    current_show.theatre_id = new_theatre_id

    db.session.commit()

    return jsonify({ 'message': 'Show updated successfully' }), 201



@shows.route('/<show_id>', methods=['DELETE'])
@admin_role_required
def delete(show_id):
    current_show = Show.query.get(show_id)

    if not current_show:
        return jsonify({'message': 'Show not found'}), 404
    
    db.session.delete(current_show)
    db.session.commit()

    return jsonify({ 'message': 'Show deleted successfully' }), 201
