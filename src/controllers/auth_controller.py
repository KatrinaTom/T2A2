from urllib import request
from datetime import timedelta
from flask import Blueprint, jsonify, request, abort
from sqlalchemy.exc import IntegrityError
from main import db, jwt, bcrypt
from models.users import User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from schemas.user_schema import UserSchema

# Create the controller for users 
auth_bp = Blueprint('auth',__name__, url_prefix='/auth')

# Log in for Admin Users
@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    # Step 1, find the user by email address
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    # Step 2, If the email exists and password is correct
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        # return UserSchema(exclude=['password']).dump(user)
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid credentials.'}, 401

# Search for all users in the database
@auth_bp.route('/users/', methods=['GET'])
@jwt_required()
def get_users():
    # print("Hello") Used for Testing API Route
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)    

# Search for only one user in the database, but the url you need to know the user id
@auth_bp.route('/user/<int:id>/', methods=['GET'])
@jwt_required()
def get_one_user(id):
    # print("Hello One User")
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404

# Create a new user, register them in the database
@auth_bp.route('/register/', methods=['POST'])
@jwt_required()
def auth_register():
    try:
        user = User(
            type = request.json['type'],
            f_name = request.json['f_name'],
            l_name = request.json['l_name'],
            address = request.json['address'],
            p_number = request.json['p_number'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            is_admin = request.json['is_admin']
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use.'}, 409

# Update a user in the database
@auth_bp.route('/update_user/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
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
        user.password = request.json.get('password') or user.password
        user.is_admin = request.json.get('is_admin') or user.is_admin
        
        db.session.commit()      
        return UserSchema().dump(user)
    else:
        return {'error': f'User can not be found with id {id}'}, 404

# Delete a user from the database, but only an admin can do this.
@auth_bp.route('/delete/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_user(id):
    authorize()

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.f_name}' deleted successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404

    # Adding in redundancy to check that only an ADMIN user can perform this function
    def authorize():
        user_id = get_jwt_identity()
        stmt = db.select(User).filter_by(id=user_id)
        user = db.session.scalar(stmt)
        if not user.is_admin:
            abort(401)

