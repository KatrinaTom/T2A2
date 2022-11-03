from main import db

# Database model - Users Table

# Note: "Type" refers to Employee or Customer

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    f_name = db.Column(db.String(128), nullable=False)
    l_name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String, nullable=False)
    p_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    # job_references = db.relationship('Job_Reference', back_populates='users')

