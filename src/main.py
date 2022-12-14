# List of all the imports. Main working file is main.py
import os
from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.job_controller import job_bp
from controllers.auth_controller import auth_bp
from controllers.product_controller import product_bp
from controllers.cli_commands import db_commands
from marshmallow.exceptions import ValidationError

def create_app():

    # Creating the Flask app object (the app core)
    app = Flask(__name__)

    # Configuring the app
    app.config.from_object("config.app_config")
    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    # Creating the database object. This is to use our own ORM
    db.init_app(app)

    # Hooking up Marshmallow to the app
    ma.init_app(app)

    # Creating the object to hash passwords
    bcrypt.init_app(app)

    # JWT initialization
    jwt.init_app(app)

    # Error handle Validation Error 
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    # Handle error when invalid request is used
    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400

    # Handle error when not found
    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    # Handle unauthorised, only is_admin can perform these actions
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You are not authorized to perform this action'}, 401

    # Handle key errors
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    # Register Blueprint
    app.register_blueprint(job_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(db_commands)

    return app


# # Routes created - Test route
# @app.route('/')
# def index():
#     return "Hello There!"

