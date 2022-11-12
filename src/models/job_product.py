from main import db, ma

association_table = db.Table(
    "job_product",
    # Base.metadata,
    db.Column("job_id", db.ForeignKey("jobs.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("products.id"), primary_key=True),
)

VALID_STATUSES = ('Quote', 'Booked', 'In_Progress', 'Cancelled', 'Completed', 'Paid')

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    units_hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates="jobs")

    products = db.relationship(
        "Product", secondary=association_table, back_populates="jobs"
    )

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(50), nullable=False)

    jobs = db.relationship(
        "Job", secondary=association_table, back_populates="products"
    )