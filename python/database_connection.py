import psycopg2

def db_connection():
    return psycopg2.connect(
        database="postgres",
        host="localhost",
        user="postgres",
        password="12092802",
        port="5432"
    )
"""
    def connectionTest(database_connection): 
        if con == 1:
            con_status = 'SUCESS CONECTION'
        else: con_status = 'CON UNSUCESS'
        return con_status
    testeResult = connectionTest(con.status)
    print(testeResult)
"""