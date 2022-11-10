# Getting Started

Build your own product and customer database.

What you will need:

* [Requirements](#requirements)
* [Set Up](#setup)
* [Create Database](#)

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