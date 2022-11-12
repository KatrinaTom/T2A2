from main import db

# Password is only for Admin users to log into the database/ provide access to the database

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
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean)
    
    # Get a list of all the job_references that the user has 
    jobs = db.relationship('Job', back_populates='user', cascade='all, delete')

    # Cascade = If user is deleted, then delete all their job_references


    
    
