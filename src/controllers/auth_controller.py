from urllib import request
from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import UserSchema

# Create the controller for users 
auth_bp = Blueprint('auth',__name__, url_prefix='/auth')


@auth_bp.route('/users/', methods=['GET'])
def get_users():
    print("Hello")
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        user = User(
            type = request.json['type'],
            f_name = request.json['f_name'],
            l_name = request.json['l_name'],
            address = request.json['address'],
            p_number = request.json['p_number'],
            email = request.json['email']
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
