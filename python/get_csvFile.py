import pandas as pd
from functions import alocate_data

initial_directory_csv = pd.read_csv('data/order_details.csv')
folder_destiny = 'order_detail'

alocate_data(folder_destiny, initial_directory_csv)