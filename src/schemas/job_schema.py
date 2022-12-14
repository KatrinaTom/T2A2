from main import ma
from marshmallow import fields, validates
from marshmallow.validate import OneOf

# Create the job_reference schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
VALID_STATUSES = ('Quote', 'Booked', 'In_Progress', 'Cancelled', 'Completed', 'Paid')

class JobSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['f_name', 'l_name'])
    products = fields.List(fields.Nested('ProductSchema'))
    status = fields.String(required=True, validate=OneOf(VALID_STATUSES))

    class Meta:
        # Fields to expose
        fields = ("id", "users_id", "status", "start_date", "end_date", "units_hours", "description", "user", "products")
        ordered = True