from strawberry import type
import strawberry
from typing import List
from api.resolvers.air_quality_status import resolve_air_quality_status
from api.resolvers.traffic_status import resolve_traffic_stats
from api.schema.grapqhl_schema import AirQualityStats, TrafficStats

@strawberry.type
class Query():
    get_traffic_stats: List[TrafficStats] = strawberry.field(resolver=resolve_traffic_stats)
    get_air_quality_stats: List[AirQualityStats] = strawberry.field(resolver=resolve_air_quality_status)