# Endpoint Documentation

Test data is located under Controllers/cli_commands.py

POSTMAN = https://www.postman.com/

Stet 1: flask db drop
Step 2: flask db create
Step 3: flask db seed

* [USERS](#users)

# Endpoints that reference: USERS<a name="users"></a>

Login as an ADMIN user 
``localhost:8080/auth/login``








** Above requires a Bearer Token for CRUD opertions. Login requires email, password and must be an Admin for security **

Search for all customers (users) in the database // GET request
``localhost:8080/auth/users``

Search for one customer(user) in the database // GET request
``localhost:8080/auth/user/1``

Register a new customer (user), create a user in the database // POST request
``localhost:8080/auth/register``

Update a customer (user) in the database // PUT or PATCH request
``localhost:8080/auth/update_user/1``

Delete a customer (user) from the database // DELETE request
``localhost:8080/auth/delete/1``

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

