from flask import Blueprint
from datetime import date
from init import db, bcrypt
from models.users import User
from models.job_product import Product, Job


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
        ),
        User(
            type='Customer',
            f_name='Peter',
            l_name='Smith',
            address='78 Road rd, FakeStreet, QLD, 4000',
            p_number='0400000002',
            email='fakeyemail@gmail.com',
        )
    ]
    db.session.add_all(new_customer)
    db.session.commit()

    # Create a landscaping service in the database
    new_product = [
        Product(
            name='Seasonal Gardening',
            description='Planting seasonable plants, fertilizing and garden tidy',
            price='110',
            size='Small'
        ),
        Product(
            name='Lawn care',
            description='Mowing, lawn edges and fertilizing',
            price='120',
            size='Small'
        )
    ]
    db.session.add_all(new_product)
    db.session.commit()

    new_jobs = [
        Job(
            status = 'Quote',
            start_date = '2023-01-02',
            end_date = '2023-01-02',
            units_hours = '5',
            description = 'Build a small garden and plant with seasonable plants.',
            user = new_customer[0],
        )
    ]
    db.session.add_all(new_jobs)
    db.session.commit()

    # 1. declared a job j1
    j1 = new_jobs[0]
    # created an array, accessing the product and storing in a variable named product. 

    # Adding product to the list of j1 products
    j1.products.append(new_product[0])
    j1.products.append(new_product[1])
    
    db.session.commit()
            

    # # Create a job_reference 
    # create_job = [
    # Job(
    #         s
    #     ),
    # Job(
    #         status = 'Booked',
    #         start_date = '2023-05-02',
    #         end_date = '2023-05-02',
    #         units_hours = '2',
    #         description = 'Mow lawn and trim edges.',
    #         user = new_customer[1],
    #         # service_order = Service[1]
    #     ),   
 

    print("Tables successfully seeded")




