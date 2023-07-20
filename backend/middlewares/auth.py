from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from extensions import db
from models.users import User

def admin_role_required(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user_id = get_jwt_identity()
            
            current_user = User.query.filter_by(id=current_user_id).first()

            if current_user.is_admin:
                return fn(*args, **kwargs)
            return jsonify({'message': 'Access denided'}), 401

        except:
            return jsonify({'message': 'Authorization required'}), 401
    return decorator