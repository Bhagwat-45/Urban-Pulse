from database.database import get_db

def initialize_bridge():
    connection = get_db()
    cursor = connection.cursor()

    sql_create_query = """
    CREATE TABLE IF NOT EXISTS bronze_events (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        event_data JSONB NOT NULL,
        ingested_at TIMESTAMPTZ DEFAULT NOW()
    );
    """

    try:
        cursor.execute(sql_create_query)
        connection.commit()
        print("Bronze Layer initialized: Table 'bronze_events' created.")
    except Exception as e:
        print(f"Migration failed: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    initialize_bridge()

    