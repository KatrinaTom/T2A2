# List of all the imports. Main working file is main.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask creation
app = Flask(__name__)

# app configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://landscaping_admin_db"

# Instances created
db = SQLAlchemy(app)


# Routes created
@app.route('/')
def index():
    return "Hello There!"

