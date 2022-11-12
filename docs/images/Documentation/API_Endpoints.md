# API Endpoint Documentation<a name="api_top"></a>

Test data is located under Controllers/cli_commands.py

POSTMAN = https://www.postman.com/

Stet 1: flask db drop
Step 2: flask db create
Step 3: flask db seed

* [USERS](#users)
* [PRODUCTS](#products)
* [JOB](#job)

# API Endpoints that reference: USERS<a name="users"></a>

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

# API Endpoints that reference: PRODUCT<a name="products"></a>

**GET /**

SEARCH for all available products

``localhost:8080/product/``

![Get Product Example](/docs/images/psql_database/get_products.png)

SEARCH for ONE type of service
``localhost:8080/product/1``

![Example of a GET request of one product](/docs/images/psql_database/get_one_product.png)

**POST /**

POST a new product to the database

``localhost:8080/product/add``

![Example of posting a new product](/docs/images/psql_database/post_product.png)

**PUT or PATCH /**

UPDATE a service in the database

``localhost:8080/service/update_service/2``

![Example of a product update](/docs/images/psql_database/update_product.png)

**DELETE /**

DELETE a service in the database

``localhost:8080/product/3``

![Example of a product deleted](/docs/images/psql_database/delete_product.png)

# API Endpoints that reference: JOB<a name="job"></a>

Endpoints that reference **JOBs**

**GET /**

GET all jobs in the database

``localhost:8080/jobs``

![Example of get all jobs](/docs/images/psql_database/get_jobs.png)

GET a specific job. Requires the id of the job

``localhost:8080/jobs/4``

![Example of one specific job](/docs/images/psql_database/job_one.png)

![Example with user and product](/docs/images/psql_database/user_get_product.png)

**POST /**

POST a new job request with a user and a product

![Example of a new job](/docs/images/psql_database/post_new_job.png)

___

[Link to the top of the page](#api_top)