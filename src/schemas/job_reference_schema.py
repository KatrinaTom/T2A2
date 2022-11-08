from main import ma

# Create the job_reference schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class Job_ReferenceSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "users_id", "status_id", "start_date", "end_date", "units_hours", "description")

# Single job reference schema, when one job reference needs to be retrieved
job_reference_schema = Job_ReferenceSchema()

# Multiple job reference schema, when more than one job reference needs to be retrieved
job_references_schema = Job_ReferenceSchema(many=True)