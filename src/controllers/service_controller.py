from urllib import request
from flask import Blueprint, jsonify, request, abort
from main import db
from models.services import Service
from sqlalchemy.exc import IntegrityError
from schemas.service_schema import ServiceSchema

# Create the controller for users
service_bp = Blueprint('service',__name__, url_prefix='/service')

# Search for all available services in the database
@service_bp.route('/available_services/', methods=['GET'])
def get_services():
    print("Hello Service")
    stmt = db.select(Service)
    services = db.session.scalars(stmt)
    return ServiceSchema(many=True).dump(services)

# # Search for only one type of service in the database, for the url you need to know the service id
@service_bp.route('/available_service/<int:id>/', methods=['GET'])
def get_one_service(id):
    print("Hello one type of service")
    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if servce:
        return ServiceSchema().dump(service)
    else:
        return {'error': f'Type of service not found with id {id}'}, 404

# Create a new landscaping service for the database
@service_bp.route('/add/', methods=['POST'])
def service_add():
    try:
        service = Service(
            name = request.json['name'],
            description = request.json['description'],
            price = request.json['price'],
            size =request.json['size']
        )

        db.session.add(service)
        db.session.commit()
        return ServiceSchema().dump(service), 201
    except IntegrityError:
        return {'error': 'Service type already exists'}, 409

# Update a service in the database
@service_bp.route('/update_service/<int:id>', methods=['PUT', 'PATCH'])
# @jwt_required()
def update_one_service(id):
    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        service.name =request.json.get('name') or service.name
        service.description = request.json.get('description') or service.description
        service.price = request.json.get('price') or service.price
        service.size = request.json.get('size') or service.size
        db.session.commit()      
        return ServiceSchema().dump(service)
    else:
        return {'error': f'The service can not be found with id {id}'}, 404

# Delete a service from the database, but only an admin can do this.
@service_bp.route('/delete/<int:id>/', methods=['DELETE'])
# @jwt_required()
def delete_one_user(id):
    # authorize()
    print("Come to delete a service")

    stmt = db.select(Service).filter_by(id=id)
    service = db.session.scalar(stmt)
    if service:
        db.session.delete(service)
        db.session.commit()
        return {'message': f"The '{service.name}' has been deleted successfully"}
    else:
        return {'error': f'The service is not found with id {id}'}, 404