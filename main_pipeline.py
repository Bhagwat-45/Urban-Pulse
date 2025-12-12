import sys
import time
from database.migrations.init_bronze_events import initialize_bridge as init_bronze
from database.migrations.init_silver_air_quality import initialize_bridge as init_silver_air
from database.migrations.init_silver_traffic import initialize_bridge as init_silver_traffic
from database.migrations.create_gold_traffic_views import initialize_bridge as init_gold_traffic
from database.migrations.create_gold_air_quality_views import initialize_bridge as init_gold_air
from generator.main import run_generator
from etl.transform.main import run_transformation
from etl.extract.gold_air_quality_referesh import referesh_gold as gold_referesh_air
from etl.extract.gold_traffic_referesh import referesh_gold as gold_referesh_traffic


def run_full_pipeline():
    print("Starting UrbanPulse Data Pipeline...")
    start_time = time.time()

    try:
        print("\n--- Phase 1: Infrastructure ---")
        init_bronze()
        init_silver_air()
        init_silver_traffic()
        init_gold_air()
        init_gold_traffic
        print("Database Schema and Views ready.")

        print("\n--- Phase 2: Ingestion ---")
        run_generator(500) 
        print("Raw IoT data ingested into Bronze Layer.")


        print("\n--- Phase 3: Transformation ---")
        run_transformation()
        print("Data cleaned and normalized into Silver Layer.")

        print("\n--- Phase 4: Analytics ---")
        gold_referesh_air()
        gold_referesh_traffic()
        print("Gold Layer refreshed. Materialized views updated.")

        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print(f"Pipeline completed successfully in {duration} seconds!")
        print("GraphQL API is now serving the latest data at http://localhost:8000/graphql")

    except Exception as e:
        print(f"\nPipeline failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_full_pipeline()