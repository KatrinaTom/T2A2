from main import db

# Database for services that the landscaping business offers

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(50), nullable=False)

    # service_requests_id = db.relationship('Service_Request', back_populates='services')

