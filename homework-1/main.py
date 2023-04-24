import csv
import psycopg2

"""Скрипт для заполнения данными таблиц в БД Postgres."""
customers = './north_data/customers_data.csv'
employees = './north_data/employees_data.csv'
orders = './north_data/orders_data.csv'

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='661104'
)

with conn:
    with conn.cursor() as cursor:

        with open(customers) as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                customer_id = row['customer_id']
                company_name = row['company_name']
                contact_name = row['contact_name']

                cursor.executemany('INSERT INTO customers VALUES (%s, %s, %s)',
                                   [(customer_id, company_name, contact_name)])

        with open(employees) as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                first_name = row['first_name']
                last_name = row['last_name']
                title = row['title']
                birth_date = row['birth_date']
                notes = row['notes']

                cursor.executemany('INSERT INTO employees VALUES (default, %s, %s, %s, %s, %s)',
                                   [(first_name, last_name, title, birth_date, notes)])

        with open(orders) as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                order_id = row['order_id']
                customer_id = row['customer_id']
                employee_id = row['employee_id']
                order_date = row['order_date']
                ship_city = row['ship_city']

                cursor.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                   [(order_id, customer_id, employee_id, order_date, ship_city)])


conn.close()