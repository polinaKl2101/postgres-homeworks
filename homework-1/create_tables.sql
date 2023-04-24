-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id varchar(20) NOT NULL,
	company_name varchar(100) NOT NULL,
	contact_name varchar(30) NOT NULL
);

CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	title text NOT NULL,
	birth_date varchar(20) NOT NULL,
	notes text NOT NULL
);

CREATE TABLE orders
(
	order_id integer NOT NULL,
	customer_id varchar(20),
	employee_id integer REFERENCES employees(employee_id) NOT NULL,
	order_date varchar(30) NOT NULL,
	ship_city varchar(50) NOT NULL

);
