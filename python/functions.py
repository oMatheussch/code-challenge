from database_connection import db_connection, db2_connection
from datetime import datetime
import pandas as pd
import os
import csv

def date_function():
    data_time = datetime.now()
    actual_data = data_time.date()
    return actual_data

def columns_type(table):
    con = db_connection()
    import_tables = con.cursor()
    import_tables.execute(f"SELECT data_type FROM information_schema.columns WHERE table_name = '{table[0]}'")
    tables_types = import_tables.fetchall()
    import_tables.close()
    con.close()
    return tables_types
    
def columns_name(table):#PENDENTE AJUSTAR AINDA
    con = db_connection()
    import_tables = con.cursor()
    import_tables.execute(f"SELECT data_type FROM information_schema.columns WHERE table_name = '{table[0]}'")
    tables_types = import_tables.fetchall()
    import_tables.close()
    con.close()
    return tables_types

def alocate_data(folder_name, df):
    directory = f'local_data/{folder_name}/'
    if os.path.exists(directory):
        df.to_csv(f'{directory}{folder_name}_{date_function()}.csv', index=False)
    else: 
        os.makedirs(directory) 
        df.to_csv(f'{directory}{folder_name}_{date_function()}.csv', index=False)   

def last_update_data(directory_check):
    lista_arquivos = os.listdir(directory_check)
    lista_arquivos.sort()
    last_arquivo = lista_arquivos[-1]
    return last_arquivo

def columns_count(directory):
    with open(directory, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            first_line = next(csv_reader)
            size = len(first_line)
            return size

def get_pk(table_name):
     conn = db2_connection()
     get_pk = conn.cursor()
     get_pk.execute(
        f"""SELECT column_name
            FROM information_schema.columns
            WHERE table_name = '{table_name}' AND column_name IN (
                SELECT column_name
                FROM information_schema.table_constraints AS tc
                JOIN information_schema.constraint_column_usage AS ccu
                USING (constraint_catalog, constraint_schema, constraint_name)
                WHERE tc.constraint_type = 'PRIMARY KEY'
                AND tc.table_name = '{table_name}'
            );""")
     pk = get_pk.fetchall()
     conn.close()
     return pk[0][0]
     
def get_all_pk(pk, table):
     conn = db2_connection()
     query = (f'SELECT {pk} FROM {table}')
     execution = conn.cursor()
     execution.execute(query)
     result = execution.fetchall()
     execution.close()
     conn.close()   
     return result

def get_csv_pk(pk, csv_file):
    csv_reader = pd.read_csv(csv_file)
    lista = csv_reader[pk].tolist()
    return lista   

