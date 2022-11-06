from main import ma

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class StatusSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "quote", "booked", "in_progress", "cancelled", "completed", "paid_in_full")
        ordered = True

# Single status to be called for a job reference
status_schema = StatusSchema()

# Can a job reference have more than one status? Not at this stage no. It can only be in one of the above at one time. 

