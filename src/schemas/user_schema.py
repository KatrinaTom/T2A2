from main import ma
from marshmallow.validate import OneOf
from marshmallow import fields
from models.users import VALID_TYPE

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class UserSchema(ma.Schema):
    job = fields.List(fields.Nested('JobSchema', exclude=['user']))
    type = fields.String(required=True, validate=OneOf(VALID_TYPE))


    class Meta:
        # Fields to expose
        fields = ("id", "type", "f_name", "l_name", "address", "p_number", "email", "password", "is_admin")
        ordered = True



