import json
import random
from datetime import datetime
from database.database import get_db

def generate_sensor_data():
    """Generates a random IoT event (Traffic or Air Quality)."""
    sensor_types = ['traffic', 'air_quality']
    s_type = random.choice(sensor_types)
    
    event = {
        "sensor_id": f"SN-{random.randint(100, 999)}",
        "type": s_type,
        "timestamp": datetime.now().isoformat(),
    }

    if s_type == 'traffic':
        event["payload"] = {
            "vehicle_count": random.randint(0, 50),
            "avg_speed": round(random.uniform(10.0, 80.0), 2)
        }
    else:
        event["payload"] = {
            "co2_level": random.randint(300, 1000),
            "pm25": round(random.uniform(0.0, 150.0), 2)
        }
    
    return event

def run_generator(count=100):
    """Generates N events and inserts them into the Bronze Layer."""
    conn = get_db()
    cursor = conn.cursor()
    
    print(f"Starting ingestion of {count} events...")
    
    try:
        for i in range(count):
            event = generate_sensor_data()
            
            event_json = json.dumps(event)
            
            cursor.execute(
                "INSERT INTO bronze_events (event_data) VALUES (%s)",
                (event_json,)
            )
            
            if i % 10 == 0:
                print(f"Ingested {i} events...")
        
        conn.commit()
        print("Successfully ingested all events into Bronze Layer.")
        
    except Exception as e:
        print(f"Ingestion failed: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_generator(100)