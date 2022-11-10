from main import ma

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class Service_RequestSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "service_id", "quanity")

# Single service request (only one type of service has been requested), when one servise is requested for the job reference needs to be retrieved
service_request_schema = Service_RequestSchema()

# Multiple services schema, when more than one service is requred for the job reference needs to be retrieved
service_requests_schema = Service_RequestSchema(many=True)