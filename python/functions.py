from database_connection import db_connection, db2_connection
from datetime import datetime
import os

def date_function():
    data_time = datetime.now()
    actual_data = data_time.date()
    return actual_data

def alocate_data(name, df):
    directory = f'local_data/{name}/'
    if os.path.exists(directory):
        df.to_csv(f'{directory}{name}_{date_function()}.csv', index=False)
    else: 
        os.makedirs(directory) 
        df.to_csv(f'{directory}{name}_{date_function()}.csv', index=False)   

def last_update_data(directory_check):
    lista_arquivos = os.listdir(directory_check)
    lista_arquivos.sort()
    last_arquivo = lista_arquivos[-1]
    return last_arquivo

def check_create_table(tables_db1, tables_db2):
    for table1 in tables_db1:
        table_exists = False
        for table2 in tables_db2:
            if table1[0] == table2[0]:
                table_exists = True
                break
        if table_exists == False:
            new_table = table1[0]
            con1 = db_connection()
            con2 = db2_connection()
            settings_new_table = con1.cursor()
            settings_new_table.execute(f"SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = '{new_table}'")
            resultado = settings_new_table.fetchall()
            creating_new_table = con2.cursor()
            creating_new_table.execute(f"CREATE TABLE {new_table} ()")
            #create_table.execute(f"CREATE TABLE {new_table} (id SERIAL PRIMARY KEY, nome VARCHAR(100) NOT NULL, idade INT);")
            con1.close()
    return resultado
