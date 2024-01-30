import os
import pandas as pd
from functions import last_update_data
from import_db_files import all_columns
from database_connection import db2_connection

"""
pasta_base = 'local_data/'
for pasta in all_columns:
    diretorio = (f'{pasta_base}{pasta}/')
    last_data = last_update_data(diretorio)
    print(last_data)
    archive = pd.read_csv(f'{diretorio}{last_data}')
    print(archive)
"""


diretorio = (f'local_data/employees/')
last_data = last_update_data(diretorio)
data_frame_export = pd.read_csv(f'{diretorio}{last_data}')
tamanho = len(data_frame_export)
print(tamanho)
for n in  range (0, tamanho):
    concat_values = ""
    for value in data_frame_export.values[n]:
        #print(value)
        tipo = type(value)
        concat_values += "'"
        concat_values += str(value)
        concat_values += "', "
        """
        if tipo == str:
            concat_values += "'"
            concat_values += value
            concat_values += "', "
        else: 
            concat_values += str(value)
            concat_values += ", "
        """
        print(concat_values)
        con2 = db2_connection()
    export_data = con2.cursor()
    export_data.execute(f'INSERT INTO employees VALUES ({concat_values});')