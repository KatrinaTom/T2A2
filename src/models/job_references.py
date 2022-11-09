from main import db
from datetime import date

# Datebase to reflect the Job_References table

VALID_STATUSES = ('Quote', 'Booked', 'In_Progress', 'Cancelled', 'Complete', 'Invoiced')

class Job_Reference(db.Model):
    __tablename__ = 'job_references'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    units_hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)

    services = db.relationship(
        'Service',
        backref='services')

    # users_id = db.relationship('User', back_populate='job_references')
    # service_requests_id = db.relationship('Service_Request', back_populate='job_references')
    # status_id = db.relationship('Status', back_populate='job_references')

