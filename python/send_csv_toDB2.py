import csv
import psycopg2
from psycopg2 import sql
from database_connection import db2_connection
from python.get_dbOne_File import tables_name
from functions import last_update_data, columns_count, columns_type, get_pk

conn = db2_connection()
for folder in tables_name:
    directory_concat = f'local_data/{folder[0]}/'
    last_data = last_update_data(directory_concat)
    csv_file_path = f'{directory_concat}{last_data}'
    print(csv_file_path)

    quantity_columns = columns_count(csv_file_path)
    qtd_columns = ''
    
    count = 0
    columns_type = columns_type(folder)
    for types in columns_type:
        count += 1
        if types[0] == 'smallint' or types == 'integer':
            type_var = 'd'
        elif types[0] == 'real':
            type_var = 'f'
        else:
            type_var = 's'

        if count + 1 > quantity_columns:
            qtd_columns += f'%{type_var}'
        else:
            qtd_columns += f'%{type_var},'
    print(qtd_columns) #apenas para teste
    def insert_data(conn, cursor, data):
        insert_query = (f'INSERT INTO {folder[0]} VALUES ({qtd_columns})')
        teste = cursor.execute(insert_query, data)
        print(teste)
        conn.commit()
    
    def import_csv_to_postgres(csv_file_path):
        conn = db2_connection()
        cursor = conn.cursor()
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                insert_data(conn, cursor, row)
        cursor.close()
        conn.close()

    import_csv_to_postgres(csv_file_path)