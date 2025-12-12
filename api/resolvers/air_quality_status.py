from database.database import get_db
from typing import List
from api.schema.grapqhl_schema import AirQualityStats

def resolve_air_quality_status() -> List[AirQualityStats]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT sensor_id, avg_co2, max_pm25, last_reading FROM gold_air_quality")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return[
        AirQualityStats(
            sensor_id=row[0],
            avg_co2=float(row[1]),
            max_pm25=float(row[2]),
            last_reading=row[3]
        )for row in rows
    ]