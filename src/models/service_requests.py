from main import db

# Database for service requests. (Many to many relationships) Joining table

class Service_Request(db.Model):
    __tablename__ = 'service_requests'

    id = db.Column(db.Integer, primary_key=True)
    quanity = db.Column(db.Integer)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)



    services = db.relationship('Service', back_populates='service_requests')
    job_references = db.relationship('Job_Reference', back_populates='service_order', cascade='all, delete')