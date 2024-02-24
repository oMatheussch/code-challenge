from database_connection import db_connection
from functions import alocate_data
import pandas as pd

con = db_connection()

import_tables = con.cursor()
import_tables.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables_name = import_tables.fetchall()

db_import = con.cursor()
#all_columns = []
for table in tables_name:
    db_import.execute(f"select * from {table[0]}")
    columns = [desc[0] for desc in db_import.description]
    
    data_select = db_import.fetchall()
    
    if len(data_select) == 0:
        print(f'Tabela {table[0]} vazia, não importada!')
    else:
        csv_file = pd.DataFrame(data_select, columns=columns)
        print(f'Tabela {table[0]} importada!')
        alocate_data(table[0], csv_file)
con.close()