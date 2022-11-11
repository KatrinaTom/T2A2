from flask import Blueprint, jsonify, request
from datetime import date
from sqlalchemy.exc import IntegrityError
from main import db
from models.job_product import Job, Product
from schemas.job_schema import JobSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


# create controller
job_bp = Blueprint('job', __name__, url_prefix='/job')

# Get all the job references available 
@job_bp.route('/jobs_all/', methods=['GET'])
# @jwt_required()
def get_jobs():
    print("Hello Job Reference List")
    stmt = db.select(Job)
    # get all the jobs from the jobs database table
    job_list = db.session.scalars(stmt)
    return JobSchema(many=True).dump(job_list)
    

# Get only one job reference, you can use limit(1), but in this case I would be looking for a particular job with status eiter booked, or searching for a date.

# Create a new job reference
@job_bp.route('/create/', methods=['POST'])
def create_job_reference():
    try:
        create_job = Job(
            user_id = request.json['user_id'],
            status = request.json['status'],
            start_date = request.json['start_date'],
            end_date = request.json['end_date'],
            units_hours = request.json['units_hours'],
            description = request.json['description'],
            # job_request_id = request.json['job_request_id'] How to connect to the association_table
        )

        db.session.add(create_job)
        db.session.commit()

        return JobSchema().dump(create_job), 201
    except IntegrityError:
        return {'error': 'Job Reference already exists'}, 409


# Delete a job from the database 
@job_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_job(id):

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f"User '{user.f_name}' deleted successfully"}
    else:
        return {'error': f'User not found with id {id}'}, 404


# Search for all jobs where a condition is met
# @job_bp('/search/', method=['GET'])
# def search_job():
#     stmt = db.select(Job).where(Job.status_id == "Booked")
#     search_job = db.session.scalars(stmt)
#     for Job in search_job:
#         print(search_job.__dict__)


# 1. Create a new job (basic stuff)
# 2. Then join the two tables together ()
@job_bp.route('/create_new', methods=['POST'])
def create_job():
        create_job =  Job(
            user_id = request.json['user_id'],
            status = request.json['status'],
            start_date = request.json['start_date'],
            end_date = request.json['end_date'],
            units_hours = request.json['units_hours'],
            description = request.json['description'],

    )
        db.session.add(create_job)
        db.session.commit()

# SELECT product_id, customer_id, 
# FROM product, sser
# WHERE product.product_id = 