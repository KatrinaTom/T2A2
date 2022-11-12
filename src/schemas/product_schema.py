from main import ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class ProductSchema(ma.Schema):
    name = fields.String(required=True, validate=And(
        Length(min=2, error='Title must be at least 2 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers and spaces are allowed')
    ))

    class Meta:
        # Fields to expose
        fields = ("id", "name", "description", "price", "size")
        ordered = True

