import psycopg2

try:
    conn = psycopg2.connect(
    dbname = "Urban-Pulse-Warehouse",
    user = "postgres",
    password = "",
    host = "localhost",
    port = "5432" 
    )

    print("The Database is connected!")
    conn.close()
except Exception as e:
    print("Couldn't connect to the Database")
    print(e)

    