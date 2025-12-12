from database.database import get_db

def initialize_bridge():
    connection = get_db()
    cursor = connection.cursor()

    sql_view_query = """
    SELECT AVG(avg_speed) AS average_speed, SUM(vehicle_count) AS vehicle_count, MAX(event_timestamp) AS last_updated, sensor_id
    FROM silver_traffic 
    GROUP BY sensor_id;
    """

    try:
        cursor.execute(f"CREATE MATERIALIZED VIEW gold_traffic_status AS {sql_view_query}")
        connection.commit()
        print("Golden Layer Traffic: View 'gold_traffic_status' created.")
    except Exception as e:
        print(f"Migration failed : {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    initialize_bridge()