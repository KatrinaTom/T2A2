from main import ma

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class ServiceSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "description", "price", "size")
        ordered = True

# Single service (only one type of service has been requested), when one servise is requested for the job reference needs to be retrieved
service_schema = ServiceSchema()

# Multiple services schema, when more than one service is requred for the job reference needs to be retrieved
services_schema = ServiceSchema(many=True)