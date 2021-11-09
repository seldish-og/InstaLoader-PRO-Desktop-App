import psycopg2
import config


def connect_database():
    connection = psycopg2.connect(
        host=config.host, 
        user=config.user,
        password=config.password,
        database=config.db_name
        )

    cursor = connection.cursor()
    return cursor

def execute_sql(cursor, sql_command):
    cursor.execute(sql_command)
    print(cursor.fetchall())

def close_connection(cursor):
    cursor.close()
    cursor.close()

cur = connect_database()
execute_sql(cur, "SELECT * FROM data")
close_connection(cur)
