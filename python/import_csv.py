import pandas as pd
from functions import date_function
import os

archive = pd.read_csv('data/order_details.csv')

directory = 'local_data/order_detail/'
archive_name = f'order_detail_{date_function()}.csv'
archive_path = os.path.join(directory, archive_name)

archive.to_csv(archive_path, index=False)
