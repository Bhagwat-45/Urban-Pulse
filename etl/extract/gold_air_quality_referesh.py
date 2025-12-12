from database.database import get_db

def referesh_gold():
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("REFRESH MATERIALIZED VIEW gold_air_quality;")
        conn.commit()
        print("Gold Traffic View Refereshed!")
    except Exception as e:
        print(f"Transformation failed: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    referesh_gold()