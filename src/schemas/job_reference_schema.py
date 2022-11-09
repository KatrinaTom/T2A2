from main import ma
from marshmallow import fields, validates

# Create the job_reference schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class Job_ReferenceSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])

    # status = fields.string(load_default=VALID_STATUSES[0])

    class Meta:
        # Fields to expose
        fields = ("id", "users_id", "status", "start_date", "end_date", "units_hours", "description", "user")
        ordered = True

# Single job reference schema, when one job reference needs to be retrieved
job_reference_schema = Job_ReferenceSchema()

# Multiple job reference schema, when more than one job reference needs to be retrieved
job_references_schema = Job_ReferenceSchema(many=True)