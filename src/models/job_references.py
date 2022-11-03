from main import db

# Datebase to reflect the Job_References table

class Job_Reference(db.Model):
    __tablename__ = 'job_references'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    units_hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)

    # users_id = db.relationship('User', back_populate='job_references')
    # service_requests_id = db.relationship('Service_Request', back_populate='job_references')
    # status_id = db.relationship('Status', back_populate='job_references')

