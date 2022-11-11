from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from main import db
from models.job_product import Job, Product
from models.users import User
from schemas.job_schema import JobSchema
from schemas.product_schema import ProductSchema
from flask_jwt_extended import jwt_required


# create controller
job_bp = Blueprint('job', __name__, url_prefix='/jobs')

# Get all the jobs available in the database
@job_bp.route('/', methods=['GET'])
@jwt_required()
def get_jobs():
    # print("Hello Job List")
    stmt = db.select(Job)
    # get all the jobs from the jobs database table
    job_list = db.session.scalars(stmt)
    return JobSchema(many=True).dump(job_list)
    
# Search for one job in the database
@job_bp.route('/<int:id>/', methods=['GET'])
@jwt_required()
def get_one_job(id):
    # print("Hello one type of product")
    stmt = db.select(Job).filter_by(id=id)
    job = db.session.scalar(stmt)
    if job:
        return JobSchema().dump(job)
    else:
        return {'error': f'Job is not found with the id {id}'}, 404

# Delete a job from the database 
@job_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_job(id):

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'Job with {id} has been deleted successfully'}
    else:
        return {'error': f'Job not found with id {id}'}, 404

# Create a new job, need a user to add the job to. 
# 1. Find the user 
# 2. Create the job - add the fields 
# 3. Add product to the job
# 4. Connect all these together to return the job, connected to the user and shows the product/s
@job_bp.route('/', methods=['POST'])
@jwt_required()
def create_job():
    stmt = db.select(User).filter_by(id=request.json['user_id'])
    user = db.session.scalar(stmt)

    stmt = db.select(Product).filter_by(id=request.json['product_id'])
    product = db.session.scalar(stmt)
    if user:
        job = Job(
            status = request.json['status'],
            start_date = request.json['start_date'],
            end_date = request.json['end_date'],
            units_hours = request.json['units_hours'],
            description = request.json['description'],
        )

        user.jobs.append(job)
        job.products.append(product)
        db.session.commit()
        return JobSchema().dump(job), 201
    else:
        return{'error': f'{request.json["user_id"]} not found to create the job'}, 404


