from flask import request, jsonify, Blueprint

from extensions import db
from models.shows import Show

from middlewares.auth import admin_role_required

shows = Blueprint('shows', __name__)

@shows.route('/', methods=['POST'])
@admin_role_required
def store():
    data = request.get_json()

    name = data['name']
    rate = data['rate']
    tags = data['tags']
    price = data['price']
    image = data['image']
    theatre_id = data['theatre_id']

    show = Show(name, rate, tags, price, image, theatre_id)

    db.session.add(show)
    db.session.commit()

    return jsonify({ 'message': 'Show created successful' }), 201


@shows.route('/<show_id>', methods=['PUT'])
@admin_role_required
def update(show_id):
    data = request.get_json()

    new_name = data['name']
    new_rate = data['rate']
    new_tags = data['tags']
    new_price = data['price']
    new_image = data['image']
    new_theatre_id = data['theatre_id']

    current_show = Show.query.get(show_id)

    if not current_show:
        return jsonify({'message': 'Show not found'}), 404
    
    current_show.name = new_name
    current_show.rate = new_rate
    current_show.tags = new_tags
    current_show.price = new_price
    current_show.image = new_image
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
