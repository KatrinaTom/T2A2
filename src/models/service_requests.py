from main import db

# Database for service requests. (Many to many relationships) Joining table

class Service_Request(db.Model):
    __tablename__ = 'service_requests'

    id = db.Column(db.Integer, primary_key=True)
    quote_price = db.Column(db.Integer, nullable=False)
    units_hours = db.Column(db.Integer, nullable=False)

    # services_id = db.relationship('Service', back_populates='service_requests')
    # job_references_id = db.relationship('Job_Reference', back_populates='service_requests')

    # services = db.relationship("Services",backref="job_references")
