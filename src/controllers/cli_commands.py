from flask import Blueprint
from datetime import date
from main import db, bcrypt
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
    admin_user = [
        User(
        type='Employee',
        f_name='admin',
        l_name='user',
        address='100 real address, businesstime, QLD, 4000',
        p_number='0401000000',
        email='business_email@gmail.com',
        password=bcrypt.generate_password_hash('batman').decode('utf-8'),
        is_admin=True
        )
    ]
    db.session.add_all(admin_user)
    db.session.commit()

    # Create a new customer in the database
    new_customer = [
        User(
        type='Customer',
        f_name='Katrina',
        l_name='Tom',
        address='153 Test Road, Testville, QLD, 4000',
        p_number='0400000001',
        email='kattest@gmail.com',
        )
    ]
    db.session.add_all(new_customer)
    db.session.commit()

    # Create a landscaping service in the database
    new_service = [
        Service(
        name='Lawn Care', 
        description='Mowing and Fertilization',
        price='80',
        size='Small'
        )
    ]
    db.session.add_all(new_service)
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




