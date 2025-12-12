import psycopg2
from api.helpers.settings import settings

db_params = {
    "host": settings.host,
    "database": settings.dbname,
    "user": settings.user,
    "password": settings.password,
    "port": settings.port
}

def get_db():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.Error) as e:
        print(f"Error connecting to the Database: {e}")
        exit(1)