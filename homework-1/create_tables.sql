-- SQL-команды для создания таблиц
--1
CREATE TABLE customer
(
 customer_id varchar(1000) PRIMARY KEY,
    company_name varchar(1000) NOT NULL,
    contact_name varchar(1000) NOT NULL
);
select * from customer;

--2 
CREATE TABLE employees
(
 employee_id int PRIMARY KEY,
    first_name varchar(1000) NOT NULL,
    last_name varchar(1000) NOT NULL,
    title varchar(1000) NOT NULL,
 birth_date varchar(1000) NOT NULL,
 notes varchar(1000) NOT NULL
);
select * from employees;

--3 
CREATE TABLE orders
(
 order_id int PRIMARY KEY,
    customer_id int REFERENCES customers(customer_id),
    employee_id int REFERENCES employees(employee_id),
 order_date varchar(1000) NOT NULL,
 ship_city varchar(1000) NOT NULL
);
select * from orders;
