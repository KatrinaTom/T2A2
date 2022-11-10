from main import ma

# Create the user schema with Marshmallow, it will provide the serialization needed for converting the data into JSON

class ProductSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "description", "price", "size")
        ordered = True
