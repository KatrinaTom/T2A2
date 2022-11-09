from main import db, ma
from datetime import date

# Datebase to reflect the Job_References table

# VALID_STATUSES = ('Quote', 'Booked', 'In_Progress', 'Cancelled', 'Complete', 'Invoiced') - default=VALID_STATUSES[0]

class Job_Reference(db.Model):
    __tablename__ = 'job_references'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    units_hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)

    user = db.relationship("User", back_populates="job_references")
    # service = db.relationship("Service", back_populates="job_references")
