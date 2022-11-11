# T2A2 - API Webserver Project<a name="toppage"></a>

Project: An admin portal for a start up Landscaping Business.

[Github](https://github.com/KatrinaTom/T2A2)

[Link to Project Tracking (Trello)](https://trello.com/invite/b/06cHHz3x/ATTI6045b9cf1328ade946408c89e0871c76D3A87865/api-web-server-project)

[Virtual WhiteBoard](https://miro.com/app/board/uXjVPVaYOmE=/)
____________________________________

## Table of Contents

### Project Overview 
* [Introduction](#introduction)
* [Brief](#brief)

### Project Planning
With the use of Trello, the project is tracked in Phases

[Phase 1: Database Design Documentation](docs/images/Documentation/Database_Design.md)

[Phase 2: Software Development](/docs/images/Documentation/Developer.md)

Includes:

* Requirements
* Set Up
* Database Creation
  
[API Endpoint Documentation](/docs/images/Documentation/API_Endpoints.md)

[Software Development Plan](#sdp)

[Architecture](#mvc)

### Resources
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

# Design Requirements

The web server must:

* Functions as intended
* Store data in a persistent data storage medium (eg. a relational database)
* Appropriately validate & sanitise any data it interacts with
* Use appropriate HTTP web request verbs - following REST conventions -  for various types of data manipulation
* Cover the full range of CRUD functionality for data within the database
An entity relationship diagram must be created to represent the database.
* The database manipulated by the web server must accurately reflect the entity relationship diagram.
* The database tables or documents must be normalised
* API endpoints must be documented in your readme
* Endpoint documentation should include: HTTP request verb, Required data where applicable, Expected response data, Authentication methods where applicable

# Code Requirements

The web server must:

* Use appropriate functionalities or libraries from the relevant programming language in its construction
* Use appropriate model methods to query the database
* Catch errors and handle them gracefully
* Returns appropriate error codes and messages to malformed requests
* Use appropriate functions or methods to sanitise & validate data
* use D.R.Y coding principles

All queries to the database must be commented with an explanation of how they work and the data they are intended to retrieve.

# Development

## Software Development Plan<a name="sdp"></a>

Below is a list of features that this project focuses on.

* Database Management System (DBMS)
* Structured Query Language (SQL), Data Definition Lanauge (DDL) Data Manipulation Language (DML) that will run SQL queries. Data Control Language (DCL)
* Entity Relationship Diagram. The first step in understanding the entities, attributes, relationships and cardinality
* Database Modelling. Transforming the concepts from the inital ERD into a database model and expressing relationships and required information.
* Practice Data Normalisation to avoid data redundancy.
* Relational Database, use of PostgreSQL and create tables with SQL.
* Data Manipulation, SQL insert, simple queries, delete, update, alter tables
* Flask - web framework for making a web application (serve requests and responses)
* Confidence in creating a web application with ORM (Object Relational Mapping) - SQLAlchemy
* Practice with CRUD (Create, Read, Update, Delete) of a databse with API Endpoints.
* Practice security of the database (Authorisation and Authentication) with Json Web Tokens. Inlcuding the use of Bearer Tokens
* Testing and validation/ error handling

## Architecture<a name="mvc"></a>

The Landscaping Admin database is structured around Model View Controller (MVC) Architectural pattern. A way or organsing a large application. Seperation of concern.

The database tables, models and schemas:

* Users
* Services
* Status
* Job_Reference
* Service_request

The relationship between the controller is that it queries the models. Where the controller will send back a response to the model to be updated or displayed to the client.

Using MVC (Model-View-Controller) architectural pattern, the next steps are to set up:

* Models Folder
* Controllers Folder
* Schemas Folder
* Update main.py with the objects and controllers
* Create Blueprint and objects
* Connecting Marshmallow for the schemas

"Purpose of a MVC Framework helps to seperate the different aspects of the application (input logic, business logic and GUI), while providing a loose coupling between these elements. This seperation helps to manage the complexity of the application."

# References<a name="reference"></a>

Visual Paradigm, 2022, "What is Model-View and Control?", accessed 3 Nov 2022, <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-model-view-control-mvc/>

Medium, 2020, "Flask with SQLAlchemy & Marshmallow", accessed 11 Nov 2022, <https://medium.com/craftsmenltd/flask-with-sqlalchemy-marshmallow-2ec34ecfd9d4>

___

[Link to the top of the page](#toppage)
