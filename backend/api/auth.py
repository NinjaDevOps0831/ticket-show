from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from extensions import db
from models.users import User

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    username = data['username']
    password = data['password']
    email = data['email']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already taken'}), 400
    
    count_user = db.session.query(User).count()

    user = User(username, False, password, email) if count_user else User(username, True, password, email)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201


@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()

    if user is not None and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
                'name': user.username,
                'email': user.email,
                'access_token': access_token
            }), 200

    else:
        return jsonify({ 'message': 'login failed' }), 401