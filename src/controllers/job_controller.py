from flask import Blueprint, jsonify, request
from datetime import date
from sqlalchemy.exc import IntegrityError
from main import db
from models.job_product import Job, Product
from schemas.job_schema import JobSchema


# create controller
job_bp = Blueprint('job', __name__, url_prefix='/job')

# Get all the job references available 
@job_bp.route('/jobs/', methods=['GET'])
# @jwt_required()
def get_jobs():
    print("Hello Job Reference List")
    stmt = db.select(Job)
    # get all the jobs from the jobs database table
    job_list = db.session.scalars(stmt)
    return JobSchema(many=True).dump(job_list)
    

# Get only one job reference, you can use limit(1), but in this case I would be looking for a particular job with status eiter booked, or searching for a date.

# Create a new job reference
# @job_reference_bp.route('/create/', methods=['POST'])
# def create_job_reference():
#     try:
#         create_job = Job_Reference(
#             user_id = request.json['user_id'],
#             status_id = request.json['status_id'],
#             start_date = request.json['start_date'],
#             end_date = request.json['end_date'],
#             units_hours = request.json['units_hours'],
#             description = request.json['description']
#         )

#         db.session.add(create_job)
#         db.session.commit()

#         return Job_ReferenceSchema().dump(create_job), 201
#     except IntegrityError:
#         return {'error': 'Job Reference already exists'}, 409

# Search for all cards where a condition is met
# @job_reference_bp('/search/', method=[])
# def search_job_reference():
#     stmt = db.select(Job_Reference).where(Job_Reference.status_id == "Booked")
#     search_job = db.session.scalars(stmt)
#     for Job_Reference in search_job:
#         print(search_job.__dict__)