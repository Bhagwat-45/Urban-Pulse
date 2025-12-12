from database.database import get_db
from typing import List
from api.schema.grapqhl_schema import TrafficStats,AirQualityStats

def resolve_traffic_stats() -> List[TrafficStats]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT sensor_id, average_speed, vehicle_count, last_updated FROM gold_traffic_status")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        TrafficStats(
            sensor_id=row[0],
            average_speed=float(row[1]),
            vehicle_count=int(row[2]),
            last_updated=row[3]
        ) for row in rows
    ]