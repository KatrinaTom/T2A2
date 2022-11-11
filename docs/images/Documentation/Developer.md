# Getting Started<a name="top"></a>

Build your own product and customer database.

What you will need:

* [Requirements](#requirements)
* [Set Up](#setup)
* [Create Database](#)
* [Test Data](#test_data)
* [CRUD](#crud)
* [Authorisation and Authentication](#auth)
* Validation and Error Handling
* Testing


# Requirements<a name="requirements"></a>

Also located under requirements.txt //
``pip install -r requirements.txt``

**Flask** // ``pip3 install flask``

**Flask-SQLAlchemy** // ``pip3 install Flask-SQLAlchemy``

**psycopy2** //
``pip3 install psycopg2``

**Marshmallow** // ``pip3 install marshmallow``

**Flask-Marshmallow** // ``pip3 install flask-marshmallow``

**marshmallow-sqlalchemy** // ``pip3 install marshmallow-sqlalchemy``

**pipenv** // ``pip3 install python-dotenv``

**Flask-Bcrypt** // ``pip install Flask-Bcrypt``

**JWT Flask Extended** // ``pip install flask-jwt-extended``

# SetUp<a name="setup"></a>

1. Git pull repository from "https://github.com/KatrinaTom/T2A2"

``git@github.com:KatrinaTom/T2A2.git``

2. Create a virtual environment and activate it

```python3 -m venv .venv && source .venv/bin/activate```

**House Keeping**

Make sure these files are available to you .env file, .flaskenv file and requirements txt file.

.flaskenv file Example

This will allow for the database to be run.

``flask run``

```
FLASK_APP=main:create_app
FLASK_DEBUG=1
FLASK_RUN_PORT=8080
```

# Create Database<a name="database"></a>

Check for PostgreSQL

```postgres --version```

Access PostgreSQL

```psql```

Database Creation.

```CREATE DATABASE landscaping_admin_db;```

Check the list of databases

```\l```

Connect to database

```\c landscaping_admin_db```

There is an ADMIN user for this database

``\c landscaping_admin_db db_dev``

... 

Example in SQL for initial table "users"

**USERS**(__user_id__, type, first_name, last_name, address, phone_number, email)

```CREATE TABLE USERS (
user_id integer PRIMARY KEY,
user_type text NOT NULL,
user_first_name text NOT NULL,
user_last_name text NOT NULL,
user_address text NOT NULL,
user_phone_number integer NOT NULL,
user_email text NOT NULL);
```

```ALTER TABLE USERS
ADD PRIMARY KEY user_id;
```

Example file of SQL [Landscaping_database](/docs/images/Documentation/landscape_db.sql)

# Test Data<a name="test_data"></a>

To access the "test" data for the database. The data is located under controllers/cli_commands.py

1. Drop the tables to start with fresh data

``flask db drop``

2. Create the tables for the database

``flask db create``

3. This command add the data located under cli_commands.py to the database. This is test data.

``flask db seed``

** With the above commands, an ADMIN user user is created.

# CRUD<a name="crud"></a>

(Create, Read, Update, Delete)

Thinking about the user and how they will interact with the database the tables **PRODUCTS**, **USERS**  and **JOB** need to have CRUD available.

This is to allow the admin user to maintain the database and manipulate the data for jobs.

# Authorisation and Authentication<a name="auth"></a>

Security is paramount in ensuring that the customers data is secure. Now that the database has endpoints that can be interacted with, it is critical to ensure that sql injection does not occur. This is already covered through the use of SQLAlchemy as the ORM, however now we need to consider other users who may have access to the database.

This is achieved through the use of **JSON Web Tokens** (JWT).

1. Additional fields added to USERS Table. is_admin and password so that a ADMIN user needs to be registered as an ADMIN user first.
2. Create a new ADMIN user API endpoint. So that authorisation can be added to the CRUD operations
3. Bearer Token is required to access the database. Expires in 1 day.
4. Function to Authorise Delete function. Currently out of scope as there is only access to admin users. However good practice to learn additional authorisation.

# Validation and Error Handling

Now that Endpoints exist, error handling needs to occur to ensure that if the wrong endpoint is hit, this is handled gracefully and displayed with JSON. This is to ensure consistency across the web application.

# Testing

Thank you for making it to the bottom of the page.

[Link to the top of the page](#top)