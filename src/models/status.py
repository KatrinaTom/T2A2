from xmlrpc.client import boolean
from main import db

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(boolean)
    booked = db.Column(boolean)
    in_progress = db.Column(boolean)
    cancelled = db.Column(boolean)
    complete = db.Column(boolean)
    paid_in_full = db.Column(boolean)

    # job_reference_id = db.relationship("Job_Reference", back_populates="status")
