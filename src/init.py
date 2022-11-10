
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# Create the database object
db = SQLAlchemy()
ma =  Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()