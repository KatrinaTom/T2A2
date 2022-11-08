from main import ma

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "type", "f_name", "l_name", "address", "p_number", "email", "password", "is_admin")
        ordered = True

# Single job reference schema, when one job reference needs to be retrieved
user_schema = UserSchema()

# Multiple job reference schema, when more than one job reference needs to be retrieved
users_schema = UserSchema(many=True)


