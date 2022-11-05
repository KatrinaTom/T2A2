from urllib import request
from flask import Blueprint, jsonify, request
from main import db
from models.users import User
from sqlalchemy.exc import IntegrityError

# Create the controller for users 
auth_bp = Blueprint('auth',__name__, url_prefix='/auth')


@auth_bp.route('/users/')
def get_users():
    stmt = db.select(User)
    users = db.session.scalar(stmt)
    return UserSchema(many=True).dump(users)

@auth_bp.route('/register/', methods=['POST'])
def auth_register():
    try:
        user = User(
            f_name = request.json['f_name'],
            l_name = request.json['l_name'],
            address = request.json['address'],
            p_number = request.json['p_number'],
            email = request.json['email']
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema().dump(user), 201
    except IntergrityError:
        return {'error': 'Email address already in use'}, 409
