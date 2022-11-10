# T2A2 - API Webserver Project

Project: An admin portal for a start up Landscaping Business.

[Link to Project Documentation](https://docs.google.com/document/d/1_dzeT4baEx9C4u5cQbMgJiJ_pbRsguKYKNvxqlA5ojc/edit?usp=sharing)

[Link to Project Tracking (Trello)](https://trello.com/invite/b/06cHHz3x/ATTI6045b9cf1328ade946408c89e0871c76D3A87865/api-web-server-project)

[Virtual WhiteBoard](https://miro.com/app/board/uXjVPVaYOmE=/)

[Github](https://github.com/KatrinaTom/T2A2)

____________________________________

## Table of Contents

### Project Overview 
* [Introduction](#introduction)
* [Brief](#brief)

### Project Planning
With the use of Trello, the project is tracked in Phases

[Phase 1: Design of Database](#phase1)

[User Story Mapping - Customer Journey](#journey)

[Phase 2: Software Development Plan](#phase2)

1. [Set Up (incl. Third Party Dependencies)](#setup)
2. [Libraries](#library)
3. [Development](#development)
4. [CRUD (Create, Read, Update, Delete)](#crud)
5. [Authorisation and Authentication](#auth)
6. Validation and Error Handling
7. Testing
8. [Deployment](#deployment)

### Resources
* Important Links
* [References](#reference)

____________________________________

# Project Overview

## Introduction<a name="introduction"></a>
To solidify your knowledge of core web server concepts and show your ability to work with web servers at a fundamental level, you should be able to write code to create a functioning web API server.

## Brief<a name="brief"></a>
Design a functioning web server in the relevant programming language. Your web server must contain valid, functioning code and adhere to the following requirements:

**Requirements**

1. Planning
2. Code

____________________________________

# Project Planning
[Link to Project Tracking (Trello)](https://trello.com/invite/b/06cHHz3x/ATTI6045b9cf1328ade946408c89e0871c76D3A87865/api-web-server-project)

## Phase 1: Design of Database<a name="phase1"></a>

[Database Design Documentation](docs/images/Documentation/Database_Design.md)


# Design Requirements
The web server must:
* function as intended
* store data in a persistent data storage medium (eg. a relational database)
* appropriately validate & sanitise any data it interacts with
* use appropriate HTTP web request verbs - following REST conventions -  for various types of data manipulation 
cover the full range of CRUD functionality for data within the database
* An entity relationship diagram must be created to represent the database.
* The database manipulated by the web server must accurately reflect the entity relationship diagram.
* The database tables or documents must be normalised
* API endpoints must be documented in your readme
* Endpoint documentation should include [HTTP request verb
Required data where applicable], [Expected response data]
* Authentication methods where applicable
  
# Development

## Phase 2: Software Development Plan<a name="phase2"></a>

An overview of this project is that it focuses on using the following:

* Database Management System (DBMS)
* Structured Query Language (SQL), Data Definition Lanauge (DDL) Data Manipulation Language (DML) that will run SQL queries. Data Control Language (DCL)
* Entity Relationship Diagram as seen in [Requirement 6](#req6). The first step in understanding the entities, attributes, relationships and cardinality
* Database Modelling as seen in [Requirement 9](#req9). Transforming the concepts from the inital ERD into a database model and expressing relationships and required information.
* Practice Data Normalisation to avoid data redundancy.
* Relational Database, use of PostgreSQL and create tables with SQL.
* Data Manipulation, SQL insert, simple queries, delete, update, alter tables
* Flask - web framework for making a web application (serve requests and responses)
* Confidence in creating a web application with ORM (Object Relational Mapping) - SQLAlchemy
* Practice with CRUD (Create, Read, Update, Delete) of a databse with API Endpoints.
* Practice security of the database (Authorisation and Authentication) with Json Web Tokens. Inlcuding the use of Bearer Tokens

## Libraries<a name="library"></a>

**Flask**

Is a lightweight WSGI web application framework in Python. It is designed to make getting started very quickly and very easily.

**marshmallow**

Is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

**Flask-Marshmallow** 

Is a thin integration layer for Flask and marshmallow that adds additional features to marshmallow.

**SQLAlchemy**

Is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

```pip3 install Flask-SQLAlchemy```

Database connection

```pip3 install psycopg2```

Configure in main.py

**Flask-SQLAlchemy**

Is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask.

**marshmallow-sqlalchemy**

Flask-Marshmallow is an integration layer for Flask that will allow for object serialisation/deserialization library. Integrated with SQLAlchemy.

```pip3 install flask-marshmallow```

```pip install marshmallow-sqlalchemy```

**pipenv**

As the dependency manager. This is located in the .env.sample file as a reference to what is required.

**Flask-Bcrypt** 

A Flask extension that provides bcrypt hashing utilities for passwords.

``pip install Flask-Bcrypt``

**JWT Flask Extended**

A Flask extenstion for JWT Manager (authentication), allowing for token creation and authentication.

``pip install flask-jwt-extended``

## Set Up (incl. Third Party Dependencies)<a name="setup"></a>

Create a virtual environment and activate it

```python3 -m venv .venv && source .venv/bin/activate```

Great a gitignore folder, main.py filder and a requirements.txt file

Install Flask

```pip3 install flask```

Set up a basic Flask app in the main.py file and test that initially it works.

## Development<a name="development"></a>

The Landscaping Admin database is structured around Model View Controller (MVC) Architectural pattern. A way or organsing a large application. Seperation of concern.

The database tables, the models:
* Users
* Services
* Status
* Job_Reference
* Service_request

The relationship between the controller is that it queries the models. Where the controller will send back a response to the model to be updated or displayed to the client.

..

From the steps above, a virtual environment is set up.

The environmental variables are configured in the .env file with the database url from postgreSQL connection. The example file is named .env.sample

Flask will run with the details updated in the .flaskenv file.

```
FLASK_APP=main
FLASK_DEBUG=True
```

Using MVC (Model-View-Controller) architectural pattern, the next steps are to set up:

* Models Folder
* Controllers Folder
* Schemas Folder
* Update main.py with the objects and controllers
* Create Blueprint and objects
* Connecting Marshmallow for the schemas

"Purpose of a MVC Framework helps to seperate the different aspects of the application (input logic, business logic and GUI), while providing a loose coupling between these elements. This seperation helps to manage the complexity of the application."

## CRUD<a name="crud"></a>

(Create, Read, Update, Delete)

Thinking about the user and how they will interact with the database the tables **SERVICES** and **CUSTOMERS** need to have CRUD available.

This is to allow the admin user to maintain the database.

## Authorisation and Authentication<a name="auth"></a>

Security is paramount in ensuring that the customers data is secure. Now that the database has endpoints that can be interacted with, it is critical to ensure that sql injection does not occur. This is already covered through the use of SQLAlchemy as the ORM, however now we need to consider other users who may have access to the database.

This is achieved through the use of **JSON Web Tokens** (JWT).

1. Additional fields added to USERS Table. is_admin and password so that a ADMIN user needs to be registered as an ADMIN user first.
2. Create a new ADMIN user API endpoint. So that authorisation can be added to the CRUD operations
3. Bearer Token is required to access the database. Expires in 1 day.
4. Function to Authorise Delete function. Currently out of scope as there is only access to admin users. However good practice to learn additional authorisation.

**Validation and Error Handling**

Now that Endpoints exist, error handling needs to occur to ensure that if the wrong endpoint is hit, this is handled gracefully and displayed with JSON. This is to ensure consistency across the web application.

1. Testing
   
..

## Deployment<a name="deployment"></a>

To access the "test" data for the database. The data is located under controllers/cli_commands.py

1. Drop the tables to start with fresh data

``flask db drop``

2. Create the tables for the database

``flask db create``

3. This command add the data located under cli_commands.py to the database. This is test data.

``flask db seed``

** With the above commands, an ADMIN user user is created.

## References<a name="reference"></a>

Visual Paradigm, 2022, "What is Model-View and Control?", accessed 3 Nov 2022, <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-model-view-control-mvc/>

