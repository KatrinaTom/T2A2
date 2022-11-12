from main import ma
from marshmallow import fields

# Create the job_reference schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class JobSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    products = fields.List(fields.Nested('ProductSchema'))
    

    # status = fields.string(load_default=VALID_STATUSES[0])

    class Meta:
        # Fields to expose
        fields = ("id", "users_id", "status", "start_date", "end_date", "units_hours", "description", "user", "products")
        ordered = True