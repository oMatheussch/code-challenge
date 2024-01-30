import psycopg2

def db_connection():
    return psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="12092802",
        port="5432"
    )

def db2_connection():
    return psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="0334791",
        port="5433"
    )
