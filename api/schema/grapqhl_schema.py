import strawberry
from datetime import datetime

@strawberry.type
class TrafficStats:
    sensor_id: str
    average_speed: float
    vehicle_count: int
    last_updated: datetime

@strawberry.type
class AirQualityStats:
    sensor_id: str
    avg_co2: float
    max_pm25: float
    last_reading: datetime