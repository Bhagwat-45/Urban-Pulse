from database.database import get_db

def initialize_bridge():
    connection = get_db()
    cursor = connection.cursor()

    sql_create_query = """
    CREATE TABLE IF NOT EXISTS silver_traffic(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sensor_id VARCHAR,
    vehicle_count INTEGER CHECK(vehicle_count>-1),
    avg_speed NUMERIC,
    event_timestamp TIMESTAMPTZ,
    bronze_ref_id UUID REFERENCES bronze_events(id)
    );
"""

    try:
        cursor.execute(sql_create_query)
        connection.commit()
        print("Silver Traffic Layer Initialized: Table 'silver_traffic' created.")
    except Exception as e:
        print(f"Migration failed : {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    initialize_bridge()