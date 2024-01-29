from datetime import datetime
import os

def date_function():
    data_time = datetime.now()
    actual_data = data_time.date()
    return actual_data

def alocate_data(name, df):
    directory = f'local_data/{name}/'
    if os.path.exists(directory):
        print('Diretório Existente')
        df.to_csv(f'{directory}{name}_{date_function()}.csv', index=False)
    else: 
        os.makedirs(directory) 
        df.to_csv(f'{directory}{name}_{date_function()}.csv', index=False)   
