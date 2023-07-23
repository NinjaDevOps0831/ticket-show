from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from jsonschema import validate

# Import db and User model
from extensions import db
from models.users import User

# Import validation JSON Schema
from validations.user_schema import register_schema, login_schema

auth = Blueprint('auth', __name__)


# Register Router
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate datas
    try:
        validate(instance=data, schema=register_schema)
    # Validate failed
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Validate Success
    username = data['username']
    email = data['email']
    password = data['password']

    same_name = User.query.filter_by(username=username).first()
    same_email = User.query.filter_by(email=email).first()

    # Check user name is taken
    if same_name or same_email:
        # Username is already taken
        return jsonify({'message': 'Username or E-mail already taken'}), 400
    
    # Check if it's admin
    count_user = db.session.query(User).count()

    user = User(username, False, password, email) if count_user else User(username, True, password, email)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Registration successful'}), 201


# Login Router
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate datas
    try:
        validate(instance=data, schema=login_schema)
    # Validate failed
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Validate Success
    username = request.json.get("username")
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()

    # Check if user exited and password is correct
    if user is not None and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({
                'name': user.username,
                'email': user.email,
                'is_admin': user.is_admin,
                'access_token': access_token
            }), 200

    # User not existed or password is not correct
    else:
        return jsonify({ 'message': 'login failed' }), 401
    