from database.database import get_db

def initialize_bridge():
    connection = get_db()
    cursor = connection.cursor()

    sql_view_query = """
    SELECT AVG(co2_level) AS avg_co2, MAX(pm25) AS max_pm25, MAX(event_timestamp) AS last_reading, sensor_id
    FROM silver_air_quality
    GROUP BY sensor_id
    """

    try:
        cursor.execute(f"CREATE MATERIALIZED VIEW gold_air_quality AS {sql_view_query}")
        connection.commit()
        print("Golden Layer Air Quality: View 'gold_air_quality' created.")
    except Exception as e:
        print(f"Migration failed : {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    initialize_bridge()