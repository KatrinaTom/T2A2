# List of all the imports. Main working file is main.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Create the database object
db = SQLAlchemy()
ma =  Marshmallow()

def create_app():

    # Creating the Flask app object (the app core)
    app = Flask(__name__)

    # Configuring the app
    app.config.from_object("config.app_config")

    # Creating the dataase object. This is to use the our own ORM
    db.init_app(app)

    # Hooking up Marshmallow to the app
    ma.init_app(app)

    # importing the controllers and acticate the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app

# # CLI Commands 
# @app.cli.command("create")
# def create_db():
#     db.create_all()
#     print("Tables created successfully")

# @app.cli.command("drop")
# def drop_db():
#     db.drop_all()
#     print("Tables dropped successfully")

# # Routes created - Test route
# @app.route('/')
# def index():
#     return "Hello There!"

