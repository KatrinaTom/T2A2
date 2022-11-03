# List of all the imports. Main working file is main.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


def create_app():

    # Creating the Flask app object (the app core)
    app = Flask(__name__)

    # Configuring the app
    app.config.from_object("config.app_config")

    # Create the database object
    db = SQLAlchemy(app)

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

