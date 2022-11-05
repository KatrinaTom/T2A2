drop table users, status, job_reference, services, service_request;

-- Table to capture all users in the database 
CREATE TABLE if not exists USERS (
    id serial PRIMARY KEY,
    user_type text NOT NULL,
    f_name varchar(128) NOT NULL,
    l_name varchar(128) NOT NULL,
    address text NOT NULL,
    p_number integer NOT NULL,
    email text NOT NULL
);

-- Table to capture all the types of services offered by the landscaping company
CREATE TABLE if not exists SERVICES (
    id serial PRIMARY KEY,
    name varchar(128) NOT NULL,
    description varchar(255) NOT NULL,
    size varchar(50) NOT NULL,
    price integer NOT NULL
);

-- Table to capture all the status of a job reference 
CREATE TABLE if not exists STATUS (
    id serial PRIMARY KEY,
    quote boolean,
    booked boolean,
    in_progress boolean,
    cancelled boolean,
    completed boolean,
    paid_in_full boolean
);

-- Joining table to identify the type of service that is requests for the job reference, calculates hours 
-- CREATE TABLE if not exists SERVICE_REQUEST (
--     id serial PRIMARY KEY,
--     services_id integer NOT NULL,
--     job_reference_id integer NOT NULL,
--     quoted_price integer NOT NULL,
--     units_hours integer NOT NULL
--     foreign key (services_id) REFERENCES services(id),
--     foreign key (job_reference_id) REFERENCES job_reference(id),
-- );

CREATE TABLE if not exists JOB_REFERENCE (
    id serial PRIMARY KEY,
    customer integer NOT NULL,
    start_date date NOT NULL,
    end_date date,
    service_request_id integer NOT NULL,
    units_hours integer NOT NULL,
    job_status integer NOT NULL,
    description varchar(128) NOT NULL
    -- FOREIGN KEY (customer) REFERENCES users(id),
    -- FOREIGN KEY (service_request_id) REFERENCES service_request(id),
    -- FOREIGN KEY (job_status) REFERENCES status(id),
);

truncate table USERS, SERVICES, JOB_REFERENCE;

INSERT into USERS (user_type, f_name, l_name, address, p_number, email) values (
    'customer', 'Kat', 'Test', '153 Test Road, Testville, QLD, 4000', '0400000001', 'kattest@gmail.com'
);

INSERT into SERVICES (name, description, size, price) values (
    'Lawn Care', 'Mowing and Fertilization', 'S', '80'
);
 