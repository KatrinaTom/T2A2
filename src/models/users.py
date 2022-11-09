from main import db

# Database model - Users Table

# Note: "Type" refers to Employee or Customer
# Password is only for Admin users to log into the database/ provide access to the database

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    f_name = db.Column(db.String(128), nullable=False)
    l_name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String, nullable=False)
    p_number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Job_Reference is a one to many relationship to user. A user can have many job_references
    job_references = db.relationship(
        'Job_Reference',
        backref='job_references')
    


