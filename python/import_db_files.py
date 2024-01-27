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

#Importando Employee
import_employee = con.cursor()
import_employee.execute("select * from employees e")
employee_select = import_employee.fetchall()

#Importando Products
import_products = con.cursor()
import_products.execute("select * from products p ")
products_select = import_products.fetchall()

#Importando Employee Territories
import_employee_territories = con.cursor()
import_employee_territories.execute("select * from employee_territories")
employee_territories_select = import_employee_territories.fetchall()

#Importando Region
import_region = con.cursor()
import_region.execute("select * from region r ")
region_select = import_region.fetchall()

#Importando Shippers
import_shippers = con.cursor()
import_shippers.execute("select * from shippers s ")
shippers_select = import_shippers.fetchall()

#Importando Suppliers
import_suppliers = con.cursor()
import_suppliers.execute("select * from suppliers s")
suppliers_select = import_suppliers.fetchall()

#Importando Territories
import_territories = con.cursor()
import_territories.execute("select * from territories t")
territories_select = import_territories.fetchall()

#Importando US States
import_us_states = con.cursor()
import_us_states.execute("select * from us_states us")
us_states_select = import_us_states.fetchall()

#Exibição no console
for res in orders_select:
    print (res)

con.close()