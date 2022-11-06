from urllib import request
from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from sqlalchemy.exc import IntegrityError
from schemas.user_schema import UserSchema

# Create the controller for users 
auth_bp = Blueprint('auth',__name__, url_prefix='/auth')

# Search for all users in the database
@auth_bp.route('/users/', methods=['GET'])
def get_users():
    # print("Hello") Used for Testing API Route
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)

# Search for only one user in the database, but the url you need to know the user id
@auth_bp.route('/user/<int:id>/', methods=['GET'])
def get_one_user(id):
    print("Hello One User")
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404

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

@auth_bp.route('/update_user/<int:id>', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        user.type =request.json.get('type') or user.type
        user.f_name = request.json.get('f_name') or user.f_name
        user.l_name = request.json.get('l_name') or user.l_name
        user.address = request.json.get('address') or user.address
        user.p_number = request.json.get('p_number') or user.p_number
        user.email = request.json.get('email') or user.email
        db.session.commit()      
        return UserSchema().dump(user)
    else:
        return {'error': f'User can not be found with id {id}'}, 404

# Delete a user from the database, but only an admin can do this.
@auth_bp.route('/delete/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_user(id):
    # authorize()
    print("Come to delete a user")

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.f_name}' deleted successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404

