import psycopg2

def create_conn():
    conn = None
    try:
        # database configuration
        conn = psycopg2.connect(
            database="your_database",
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432"
        )
        print("Database connection successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return conn

def close_conn(conn):
    conn.close()
    print("Database connection closed")