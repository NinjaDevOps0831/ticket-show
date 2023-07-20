from flask import request, jsonify, Blueprint

from extensions import db
from models.theatres import Theatre

from middlewares.auth import admin_role_required

theatres = Blueprint('theatres', __name__)


@theatres.route('/', methods=['POST'])
@admin_role_required
def store():
    data = request.get_json()

    name = data['name']
    place = data['place']
    capacity = data['capacity']
    image = data['image']

    theatre = Theatre(name, place, capacity, image)

    db.session.add(theatre)
    db.session.commit()

    return jsonify({ 'message': 'Theatre created successful' }), 201


@theatres.route('/<theatre_id>', methods=['PUT'])
@admin_role_required
def update(theatre_id):
    data = request.get_json()

    new_name = data['name']
    new_place = data['place']
    new_capacity = data['capacity']
    new_image = data['image']

    current_theatre = Theatre.query.get(theatre_id)

    if not current_theatre:
        return jsonify({'message': 'Theatre not found'}), 404
    
    current_theatre.name = new_name
    current_theatre.place = new_place
    current_theatre.capacity = new_capacity
    current_theatre.image = new_image

    db.session.commit()

    return jsonify({ 'message': 'Theatre updated successfully' }), 201


@theatres.route('/<theatre_id>', methods=['DELETE'])
@admin_role_required
def delete(theatre_id):
    current_theatre = Theatre.query.get(theatre_id)

    if not current_theatre:
        return jsonify({'message': 'Theatre not found'}), 404
    
    db.session.delete(current_theatre)
    db.session.commit()

    return jsonify({ 'message': 'Theatre deleted successfully' }), 201
