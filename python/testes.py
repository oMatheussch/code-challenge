import csv
from functions import get_pk, get_all_pk, last_update_data, get_csv_pk, columns_type
from database_connection import db2_connection
from python.get_dbOne_File import tables_name


for folder in tables_name:
    directory_concat = f'local_data/{folder[0]}/'
    last_data = last_update_data(directory_concat)
    csv_file_path = f'{directory_concat}{last_data}'
    print(csv_file_path)

    def import_csv_to_postgres(csv_file_path):
            conn = db2_connection()
            cursor = conn.cursor()

            pk = get_pk(folder[0])#BUSCA A COLUNA QUE É PK DENTRO DA TABELA
            data = get_all_pk(pk, folder[0])#BUSCA A PK ESPECÍFICA DA LINHA NO DB

            position_pk_csv = get_csv_pk(pk, csv_file_path)#BUSCA A POSIÇAO DA PK DENTRO DO CSV
            print('Posição da PK: ', position_pk_csv)

            print('Tabela: ',folder[0])
            print('PK: ', pk)
            print('Todas as PK`s: ', data)

            print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    for dados in data:
                        print(row[position_pk_csv])
                        if row[position_pk_csv] == dados:
                            update = (f'UPDATE {folder[0]} SET ')
                            print('PK EXISTENTE')
                            print(row[position_pk_csv])
                        else: 
                             columns_type = columns_type(folder)
                             insert = (f'INSERT INTO {folder[0]} VALUES ();')
                             print('PK NÃO EXISTENTE')
                        break
                
            cursor.close()
            conn.close()

    import_csv_to_postgres(csv_file_path)
