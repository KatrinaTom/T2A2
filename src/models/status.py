from xmlrpc.client import boolean
from main import db

class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.boolean)
    booked = db.Column(db.boolean)
    in_progress = db.Column(db.boolean)
    cancelled = db.Column(db.boolean)
    complete = db.Column(db.boolean)
    paid_in_full = db.Column(db.boolean)

    # job_reference_id = db.relationship("Job_Reference", back_populates="status")
