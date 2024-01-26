from database_connection import db_connection

#Importando Conexão
con = db_connection

#Importando Orders
import_orders = con.cursor()
import_orders.execute("SELECT * FROM orders")
orders_select = import_orders.fetchall()

for res in result:
    print (res)