import psycopg


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="ml_platform",
        user="ml_user",
        password="ml_password",
    )

    return connection
