import json
from database.database import get_db

def run_transformation():
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, event_data FROM bronze_events")
        results = cursor.fetchall()

        for row in results:
            bronze_id = row[0]
            data = row[1]
            
            if data.get('type') == 'traffic':
                sensor_id = data.get('sensor_id')
                timestamp = data.get('timestamp')
                payload = data.get('payload', {})
                
                vehicle_count = payload.get('vehicle_count')
                avg_speed = payload.get('avg_speed')

                insert_query = """
                    INSERT INTO silver_traffic (
                        bronze_ref_id, 
                        sensor_id, 
                        vehicle_count, 
                        avg_speed, 
                        event_timestamp
                    ) VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (bronze_ref_id) DO NOTHING;
                """
                
                cursor.execute(insert_query, (
                    bronze_id, 
                    sensor_id, 
                    vehicle_count, 
                    avg_speed, 
                    timestamp
                ))

            elif data.get('type') == 'air_quality':
                sensor_id = data.get('sensor_id')
                timestamp = data.get('timestamp')
                payload = data.get('payload', {})

                pm25 = payload.get('pm25')
                co2_level = payload.get('co2_level')

                insert_query = """
                    INSERT INTO silver_air_quality(
                    bronze_ref_id,
                    sensor_id,
                    pm25,
                    co2_level,
                    event_timestamp
                    )VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (bronze_ref_id) DO NOTHING;
                """
                cursor.execute(insert_query, (
                    bronze_id, 
                    sensor_id, 
                    pm25, 
                    co2_level, 
                    timestamp
                ))

        conn.commit()
        print("Traffic data transformation complete.")

    except Exception as e:
        print(f"Transformation failed: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_transformation()