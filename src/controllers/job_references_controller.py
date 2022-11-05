# from flask import Blueprint, jsonify, request
# from main import db
# from models.job_references import Job_Reference
# from schemas.job_reference_schema import Job_ReferenceSchema

# # create controller
# job_references_bp = Blueprint('job_references', __name__, url_prefix='/job_references')

# # the GET routes endpoint
# @job_references.route('/', methods=['GET'])
# def get_job_references():
#     # get all the jobs from the job_references database table
#     job_references_list = Job_Reference.query.all()
#     # Convert the job references from the database into a JSON format and store them in result
#     result = Job_ReferenceSchema.dump(job_references_list)
#     # return the data in JSON format
#     return jsonify(result)
#     # return "List of Job References"

# # The POST route endpoint
# @job_references.route('/', methods=['POST'])
# def create_job_reference():
#     # Create a new job reference
#     job_reference_fields = Job_ReferenceSchema.load(request.json)

#     new_job_reference = Job_Reference()
#     new_job_reference.start_date = job_reference_fields["start_date"]
#     new_job_reference.end_date = job_reference_fields["end_date"]
#     new_job_reference.units_hours = job_reference_fields["units_hours"]
#     new_job_reference.description = job_reference_fields["description"]
    
#     # Add to the database and commit
#     db.session.add(new_job_reference)
#     db.session.commit()
#     # return the job reference in the response
#     return jsonify(Job_ReferenceSchema.dump(new_job_reference))
#     # return "New Job Reference created"

#     # CRUD resource with a DELETE method
# # @job_references.route('/<int:id>/', methods=['DELETE'])
# # def delete_job_reference(id):