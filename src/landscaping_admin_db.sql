drop table users, status, job_reference, services, service_request;

CREATE TABLE USERS (
    user_id serial PRIMARY KEY,
    user_type text NOT NULL,
    user_first_name varchar(128) NOT NULL,
    user_last_name varchar(128) NOT NULL,
    user_address text NOT NULL,
    user_phone_number integer NOT NULL,
    user_email text NOT NULL
);

CREATE TABLE STATUS (
    status_id integer PRIMARY KEY,
    quote boolean,
    booked boolean,
    in_progress boolean,
    cancelled boolean,
    completed boolean,
    paid_in_full, boolean
);

CREATE TABLE JOB_REFERENCE (
    job_reference_id serial PRIMARY KEY,
    start_date date NOT NULL,
    end_date date,
    service_request_id integer NOT NULL,
    units_hours integer NOT NULL,
    status_id integer NOT NULL,
    description varchar(128) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USERS (user_id),
    FOREIGN KEY (status_id) REFERENCES STATUS (status_id),
    FOREIGN KEY (service_request_id) REFERENCES SERVICE_REQUEST (service_request_id)
);


CREATE TABLE SERVICES (
    service_type_id integer PRIMARY KEY,
    name varchar(128) NOT NULL,
    description varchar(255) NOT NULL,
    size varchar(50) NOT NULL,
    price integer NOT NULL
);

CREATE TABLE SERVICE_REQUEST (
    service_request_id serial PRIMARY KEY,
    services_id integer NOT NULL,
    job_reference_id integer NOT NULL,
    quoted_price integer NOT NULL,
    units_hours integer NOT NULL,
    FOREIGN KEY (services_id) REFERENCES SERVICES (services_id)
);
