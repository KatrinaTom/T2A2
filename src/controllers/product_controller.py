from flask import Blueprint, jsonify, request, abort
from main import db
from models.job_product import Product
from sqlalchemy.exc import IntegrityError
from schemas.product_schema import ProductSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

# Create the controller for users
product_bp = Blueprint('product',__name__, url_prefix='/product')

# Search for all available products in the database
@product_bp.route('/available_products/', methods=['GET'])
@jwt_required()
def get_products():
    # print("Hello Product")
    stmt = db.select(Product)
    products = db.session.scalars(stmt)
    return ProductSchema(many=True).dump(products)

# # Search for only one type of product in the database, for the url you need to know the product id
@product_bp.route('/available_product/<int:id>/', methods=['GET'])
@jwt_required()
def get_one_product(id):
    # print("Hello one type of product")
    stmt = db.select(Product).filter_by(id=id)
    product = db.session.scalar(stmt)
    if product:
        return ProductSchema().dump(product)
    else:
        return {'error': f'Type of product not found with id {id}'}, 404

# Create a new landscaping product for the database
@product_bp.route('/add/', methods=['POST'])
@jwt_required()
def product_add():
    try:
        product = Product(
            name = request.json['name'],
            description = request.json['description'],
            price = request.json['price'],
            size =request.json['size']
        )

        db.session.add(product)
        db.session.commit()
        return ProductSchema().dump(product), 201
    except IntegrityError:
        return {'error': 'Product type already exists'}, 409

# Update a product in the database
@product_bp.route('/update_product/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_product(id):
    stmt = db.select(Product).filter_by(id=id)
    product = db.session.scalar(stmt)
    if product:
        product.name =request.json.get('name') or product.name
        product.description = request.json.get('description') or product.description
        product.price = request.json.get('price') or product.price
        product.size = request.json.get('size') or product.size
        db.session.commit()      
        return ProductSchema().dump(product)
    else:
        return {'error': f'The product can not be found with id {id}'}, 404

# Delete a product from the database, but only an admin can do this.
@product_bp.route('/delete/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_user(id):
    authorize()
    print("Come to delete a product")

    stmt = db.select(Product).filter_by(id=id)
    product = db.session.scalar(stmt)
    if product:
        db.session.delete(product)
        db.session.commit()
        return {'message': f"The '{product.name}' has been deleted successfully"}
    else:
        return {'error': f'The product is not found with id {id}'}, 404

 # Adding in redundancy to check that only an ADMIN user can perform this function
def authorize():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)