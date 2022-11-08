# List of all the imports. Main working file is main.py
from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
import os


# Create the database object
db = SQLAlchemy()
ma =  Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():

    # Creating the Flask app object (the app core)
    app = Flask(__name__)

    # Configuring the app
    app.config.from_object("config.app_config")

    # Creating the database object. This is to use the our own ORM
    db.init_app(app)

    # Hooking up Marshmallow to the app
    ma.init_app(app)

    # Creating the object to hash passwords
    bcrypt.init_app(app)

    # JWT initialization
    jwt.init_app(app)

    # Error handle Validation Error 
    # @app.errorhandler(ValidationError)
    # def validation_error(err):
    #     return {'error': err.messages}, 400

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


    # importing the controllers and acticate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app


# # Routes created - Test route
# @app.route('/')
# def index():
#     return "Hello There!"

