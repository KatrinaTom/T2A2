from init import db

# Database model for Users (This includes customers and emmployees)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    f_name = db.Column(db.varchar(128), nullable=False)
    l_name = db.Column(db.varchar(128), nullable=False)
    address = db.Column(db.String, nullable=False)
    p_number = db.Column(db.Ineger, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)



