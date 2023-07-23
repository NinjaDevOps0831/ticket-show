from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from jsonschema import validate

# Import db and Theatre model
from extensions import db
from models.theatres import Theatre

# Import auth middleware
from middlewares.auth import admin_role_required

# Import validation JSON Schema
from validations.theatre_schema import schema

theatres = Blueprint('theatres', __name__)


# Get Router
@theatres.route('/', methods=['GET'])
@jwt_required()
def get_all():
    theatres = Theatre.query.all()
    theatres_data = [
        {
            'id': theatre.id,
            'name': theatre.name,
            'place': theatre.place,
            'capacity': theatre.capacity
        }
        for theatre in theatres
    ]

    return jsonify(theatres_data), 200


@theatres.route('/<theatre_id>', methods=['GET'])
@jwt_required()
def get_by_id(theatre_id):
    current_theatre = Theatre.query.get(theatre_id)

    theatre_data = {
        'id': current_theatre.id,
        'name': current_theatre.name,
        'place': current_theatre.place,
        'capacity': current_theatre.capacity
    }

    return jsonify(theatre_data), 200

# Store Router
@theatres.route('/', methods=['POST'])
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
    place = data['place']
    capacity = data['capacity']

    theatre = Theatre(name, place, capacity)

    db.session.add(theatre)
    db.session.commit()

    return jsonify({ 'message': 'Theatre created successful' }), 201



# Update Router
@theatres.route('/<theatre_id>', methods=['PUT'])
@admin_role_required
def update(theatre_id):
    data = request.get_json()

     # Validate datas
    try:
        validate(instance=data, schema=schema)
    # Validate failed
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Validate Success
    new_name = data['name']
    new_place = data['place']
    new_capacity = data['capacity']

    current_theatre = Theatre.query.get(theatre_id)

    # Check theatre is existed
    if not current_theatre:
        # Theatre is not existed
        return jsonify({'message': 'Theatre not found'}), 404
    
    # Theatre is existed
    current_theatre.name = new_name
    current_theatre.place = new_place
    current_theatre.capacity = new_capacity

    db.session.commit()

    return jsonify({ 'message': 'Theatre updated successfully' }), 201



# Delete Router
@theatres.route('/<theatre_id>', methods=['DELETE'])
@admin_role_required
def delete(theatre_id):
    current_theatre = Theatre.query.get(theatre_id)

    # Check theatre is existed
    if not current_theatre:
        # Theatre is not existed
        return jsonify({'message': 'Theatre not found'}), 404
    
    # Theatre is existed
    db.session.delete(current_theatre)
    db.session.commit()

    return jsonify({ 'message': 'Theatre deleted successfully' }), 201
