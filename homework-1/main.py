"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="north_data",
    user="postgres",
    password="0407",
    port="5432"
)

cur = conn.cursor()

# Employees
with open("north_data/employees_data.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
            (row["employee_id"], row["first_name"], row["last_name"],
             row["title"], row["birth_date"], row["notes"])
        )

# Customers
with open("north_data/customers_data.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s)",
            (row["customer_id"], row["company_name"], row["contact_name"])
        )

# Orders
with open("north_data/orders_data.csv", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        cur.execute(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
            customer_id int REFERENCES customers(customer_id),
            employee_id int REFERENCES employees(employee_id),
            (row["order_id"], row["customer_id"], row["employee_id"],
             row["order_date"], row["ship_city"])
        )

conn.commit()

cur.close()
conn.close()

print("Данные успешно загружены!")
