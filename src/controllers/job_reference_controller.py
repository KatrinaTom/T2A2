from flask import Blueprint, jsonify, request
from main import db
from models.job_references import Job_Reference
from schemas.job_reference_schema import Job_ReferenceSchema
from sqlalchemy.exc import IntegrityError

# create controller
job_reference_bp = Blueprint('job_reference', __name__, url_prefix='/job_reference')

# # Get all the job references available 
# @job_reference_bp.route('/', methods=['GET'])
# def get_job_references():
#     print("Hello Job Reference List")
#     # get all the jobs from the job_references database table
#     job_references_list = Job_Reference.query.all()
#     # Convert the job references from the database into a JSON format and store them in result
#     result = Job_ReferenceSchema.dump(job_references_list)
#     # return the data in JSON format
#     return jsonify(result)
#     # return "List of Job References"

# Create a new job reference
@job_reference_bp.route('/create/', methods=['POST'])
def create_job_reference():
    try:
        create_job = Job_Reference(
            start_date = request.json['start_date'],
            end_date = request.json["end_date"],
            units_hours = request.json["units_hours"],
            description = request.json["description"]
        )

        db.session.add(create_job)
        db.session.commit()

        return Job_ReferenceSchema().dump(create_job), 201
    except IntegrityError:
        return {'error': 'Job Reference already exists'}, 409