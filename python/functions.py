from datetime import datetime

def date_function():
    data_time = datetime.now()
    actual_data = data_time.date()
    return actual_data