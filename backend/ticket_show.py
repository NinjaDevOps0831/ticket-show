from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from api.auth import auth

from extensions import jwt, db

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'SECRET'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket-show.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)

    migrate = Migrate(app, db)

    jwt.init_app(app)


    app.register_blueprint(auth, url_prefix='/api/auth')

    # 404 error handler
    @app.errorhandler(404)
    def not_found(e):
        return {"message": "resource not found", "error": 404}, 404

    # 500 error handler
    @app.errorhandler(500)
    def internal_server_error(e):
        return {"message": "internal server error", "error": 500}, 500
    return app
