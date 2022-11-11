# Endpoint Documentation

Test data is located under Controllers/cli_commands.py

POSTMAN = https://www.postman.com/

Stet 1: flask db drop
Step 2: flask db create
Step 3: flask db seed

* [USERS](#users)

# Endpoints that reference: USERS<a name="users"></a>

**POST /**

LOGIN as an ADMIN user

``localhost:8080/auth/login``

Request Example
![Request Example](/docs/images/psql_database/auth_login.png)

Response Example
![Response Example](/docs/images/psql_database/auth_response.png)

** Above requires a Bearer Token for CRUD opertions. Login requires email, password and must be an Admin for security **

POST (create) a new ADMIN to the database

``localhost:8080/auth/register_admin/``

![Example of JSON request](/docs/images/psql_database/post_admin_new.png)


POST (create) a new customer (user) in the database

``localhost:8080/auth/register``

![Example of POST request for new user](/docs/images/psql_database/post_new_user.png)

**GET /**

SEARCH for all customers (users) in the database

``localhost:8080/auth/users``

Example of Bearer Token and response of users in the user database

![Bearer Token Example](/docs/images/psql_database/bearer_token.png)

SEARCH for one customer (user) in the database
``localhost:8080/auth/user/1``

!Example request of one user[](/docs/images/psql_database/get_user_id.png)

**PUT or PATCH /**

UPDATE a customer (user) in the database // PUT or PATCH request
``localhost:8080/auth/user/6``

![Update a user Example](/docs/images/psql_database/update_user.png)

**DELETE /**

Delete a customer (user) from the database // DELETE request
``localhost:8080/auth/user/1``

![Delete a user Example](/docs/images/psql_database/delete_user.png)

...

*As a user*

*I want to create a new service in the database*

*So that I can add maintain more services for my customers*


Endpoints that reference **SERVICES:**

Search for all available services // GET request
``localhost:8080/service/available_services``

Search for one type of service // GET request
``localhost:8080/service/available_service/2``

Add a new type of service to the database // POST request
``localhost:8080/service/add``

Update a service in the database // PUT or PATCH request
``localhost:8080/service/update_service/2``

Delete a service in the database // DELETE request
``localhost:8080/service/delete/1``

...

*As a user*

*I want to the ability to maintain a job reference*

*So that I can create, track and delete job references*

Endpoints that reference **JOB_REFERENCE**

``localhost:8080/job_reference/jobs/`` // GET request


Create a new job reference in the database // POST request
``localhost:8080/job_reference/create``

