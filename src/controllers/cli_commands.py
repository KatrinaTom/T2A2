from flask import Blueprint
from datetime import date
from main import db
from models.users import User
from models.services import Service
from models.job_references import Job_Reference



db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables successfully created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():

    # Create an admin user = True
    admin_user = User(
        f_name = 'admin',
        l_name = 'user',
        address = '100 real address, businesstime, QLD, 4000',
        p_number = '0401000000',
        email = 'business_email@gmail.com',
        is_admin = True
        )
    db.session.add_all(admin_user)
    db.session.commit()

    # create_job = Job_Reference(
    #         user_id = '6',
    #         status_id = 'Quote',
    #         start_date = '7/11/2022',
    #         end_date = '7/11/2022',
    #         units_hours = '5',
    #         description = 'Build a small garden and plant with seasonable plants.'
    # )
    # db.session.add_all(create_job)
    # db.session.commit()

    print("Tables successfully seeded")





