from database_connection import db_connection, db2_connection
import functions
import pandas as pd
import csv

con = db_connection()

cursor = con.cursor()
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
cursor.execute(query)
tables_name = cursor.fetchall()

#ATÉ ESSE MOMENTO, REALIZEI O SELECT E BUSQUEI TODAS AS TABELAS DENTRO DO DB PRIMÁRIO

for folder in tables_name:
    directory_concat = f'local_data/{folder[0]}/'
    last_data = functions.last_update_data(directory_concat)
    csv_file_path = f'{directory_concat}{last_data}'
    #print(csv_file_path)

#ATÉ AQUI, REALIZEI A CONCATENAÇÃO E IDENTIFIQUEI O ÚLTIMO ARQUIVO SALVO LOCALMENTE
    
#AGORA PRECISO PEGAR O ARQUIVO, ABRI-LO E VERIFICAR SE TEM CONTEÚDO DENTRO.
#SE TIVER, PRECISO VERIFICAR SE ALGUMA LINHA JÁ EXISTIR, PRECISO FAZER UM UPDATE, SE NÃO EU PRECISO REALIZAR UM INSERT   
    #csv_reader = pd.read_csv(csv_file_path)
    def test(csv_file_path):
        with open (csv_file_path, 'r') as csv_content:
            csv_content = csv.reader(csv_content)
            next(csv_content, None)
            #if csv_reader.isnull().values.any(): #AQUI VERIFICA SE É NULLO OU NÃO
            #    print(f'Arquivo: ({csv_file_path}) está vazio!')
            for row in csv_content:
                if row: #AQUI VERIFICA SE É NULLO OU NÃO
                    return False
                else: 
                    return True
    
    pk_name = functions.get_pk(folder[0])       
    def get_all_pk(pk, table): #BUSCO TODAS AS PK'S do DB2
         conn = db2_connection()
         query = (f'SELECT {pk} FROM {table}')
         execution = conn.cursor()
         execution.execute(query)
         primare_keys = execution.fetchall()
         execution.close()
         conn.close()   
         return primare_keys
    
    all_db_pk = get_all_pk(pk_name, folder[0])
    csv_pk = functions.get_csv_pk(pk_name, csv_file_path)
    
    print(csv_pk)  
            #print(all_csv_pk)          


        #print(csv_reader)