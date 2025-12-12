# UrbanPulse: Smart City Telemetry Platform

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-elephant)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![GraphQL](https://img.shields.io/badge/GraphQL-Strawberry-pink)
![Architecture](https://img.shields.io/badge/Medallion-Architecture-orange)

UrbanPulse is a high-throughput telemetry platform designed to ingest, transform, and serve smart-city IoT sensor data.  
It follows the Medallion Architecture (Bronze → Silver → Gold) in PostgreSQL and exposes analytical datasets through a GraphQL API.

## Architecture

### Bronze Layer (Raw)
- High-speed ingestion of JSONB events  
- Append-only logs  
- No validation or transformation  

### Silver Layer (Clean)
- Deduplication and type normalization  
- Data quality validation  
- Handling of invalid or late-arriving events  

### Gold Layer (Analytics)
- Star-schema optimized for analytical workloads  
- Pre-aggregated traffic and air-quality metrics  

## Tech Stack
- PostgreSQL 15+  
- Python (custom ETL orchestration)  
- FastAPI + Strawberry GraphQL  
- psycopg2-binary  

## Project Structure

```
urban_pulse/
├── api/            # FastAPI + GraphQL schema and resolvers
├── database/       # Migrations and SQL artifacts
├── etl/            # Extract and Transform pipeline
├── generator/      # Mock IoT event generator
└── requirements.txt
```

## Getting Started

### 1. Installation
```bash
git clone https://github.com/yourusername/urban_pulse.git
cd urban_pulse
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Database Configuration
Create a `.env` file:

```
DB_NAME=urban_pulse_warehouse
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```

Initialize schema:

```bash
python -m database.migrations.init_db
```

## Usage

### Generate Mock IoT Events
```bash
python -m generator.main --events 1000
```

### Run ETL Pipeline
```bash
python -m etl.main
```

### Start GraphQL API
```bash
uvicorn api.main:app --reload
```

GraphQL Playground: http://localhost:8000/graphql

## Sample GraphQL Query

```graphql
query {
  getTrafficStats(limit: 10) {
    timestamp
    sensorId
    totalVehicles
    avgSpeed
  }
}
```

## Roadmap
- Partitioning for Silver tables  
- Redis caching  
- Docker Compose environment  
- Kafka-based real-time ingestion  

## Contributing
- Fork the repository  
- Create a feature branch  
- Commit your changes  
- Open a pull request  
