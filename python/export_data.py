from database_connection import db_connection, db2_connection

con2 = db2_connection()

#Tables Check
public_tables = con2.cursor()
public_tables.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
get_tables = public_tables.fetchall()

con = db_connection()

import_tables = con.cursor()
import_tables.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables_select = import_tables.fetchall()

#result = check_create_table(tables_select, get_tables)
print(tables_select)
#print(result)   