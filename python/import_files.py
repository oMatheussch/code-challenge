from database_connection import db_connection

con = db_connection()

#Importando Orders
import_orders = con.cursor()
import_orders.execute("SELECT * FROM orders")
orders_select = import_orders.fetchall()

#Importando Categorias
import_categories = con.cursor()
import_categories.execute("select * from categories")
categories_select = import_categories.fetchall()

#Importando Customer Demo
import_customers_demo = con.cursor()
import_customers_demo.execute("select * from customer_customer_demo ccd")
customer_demo_select = import_customers_demo.fetchall()

#Importando Customer Demographics
import_customer_demographics = con.cursor()
import_customer_demographics.execute("select * from customer_demographics")
customer_demographics_select = import_customer_demographics.fetchall()

#Importando Customer
import_customer = con.cursor()
import_customer.execute("select * from customers")
customer_select = import_customer.fetchall()

#Importando Employee Territories
import_employee_territories = con.cursor()
import_employee_territories.execute("select * from employee_territories")
employee_territories_select = import_employee_territories.fetchall()

#Exibição no console
for res in orders_select:
    print (res)

con.close()