from database_connection import db_connection
from functions import alocate_data
import pandas as pd

con = db_connection()

import_tables = con.cursor()
import_tables.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables_select = import_tables.fetchall()

db_import = con.cursor()
all_columns = []
for table in tables_select:
    db_import.execute(f"select * from {table[0]}")
    columns = [desc[0] for desc in db_import.description]
    all_columns.append(table[0])
    data_select = db_import.fetchall()
    data_frame = pd.DataFrame(data_select, columns=columns)
    alocate_data(table[0], data_frame)

con.close()