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


# # Database model - Users Table
# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(50), nullable=False)
#     f_name = db.Column(db.String(128), nullable=False)
#     l_name = db.Column(db.String(128), nullable=False)
#     address = db.Column(db.String, nullable=False)
#     p_number = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String, nullable=False, unique=True)



# # Routes created - Test route
# @app.route('/')
# def index():
#     return "Hello There!"

