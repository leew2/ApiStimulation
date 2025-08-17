# Post data to air_quality table in env.db
import json

# imported from assignment
# scripts/generate_fake_data.py
import os
from fetch_db import get_db_connection
import pandas as pd
import time
from fetch_db import create_db

# main frame of API --------------------------------------------------------------
class api:
    # due to limited time, no search for specific value
    def GET(sortby="date"): # returns all data sorted by a specific column
        if db_checks("./data/env.db"):
            df = get_data_df()
            return df.sort_values(by=sortby)
        return {"error": "Database check failed."}

    def POST(data=None):
        if isinstance(data, str):
            data = json.loads(data)
            required = ["station_id", "date", "aqi", "co2_ppm"]
            for key in required:
                if key not in data:
                    print(f"Missing field: {key}")
                    return 404
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO air_quality (station_id, date, aqi, co2_ppm) VALUES (?, ?, ?, ?)",
                (data["station_id"], data["date"], data["aqi"], data["co2_ppm"])
            )
            conn.commit()
            conn.close()
            print(f"POST: Data inserted successfully {data}")
            return 200
        except Exception as e:
            print(f"POST failed: {e}")
            return 404
    
    def PUT(data=None):
        if isinstance(data, str):
            data = json.loads(data)
            required = ["station_id", "date", "air_quality", "co2_ppm"]
            for key in required:
                if key not in data:
                    print(f"Missing field: {key}")
                    return 404
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE air_quality SET aqi = ?, co2_ppm = ? WHERE station_id = ? AND date = ?",
                (data["aqi"], data["co2_ppm"], data["station_id"], data["date"])
            )
            conn.commit()
            conn.close()
            print(f"PUT: Data successfully updated {data}")
            return 200
        except Exception as e:
            print(f"PUT failed: {e}")
            return 404
        
    def DELETE(data=None):
        if isinstance(data, str):
            data = json.loads(data)
            required = ["station_id", "date"]
            for key in required:
                if key not in data:
                    print(f"Missing field: {key}")
                    return 404
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM air_quality WHERE station_id = ? AND date = ?",
                (data["station_id"], data["date"])
            )
            conn.commit()
            conn.close()
            print(f"DELETE: Data deleted successfully {data}")
            return 200
        except Exception as e:
            print(f"DELETE failed: {e}")
            return 404
        
# end of api() --------------------------------------------------------------






# create data from db -------------------------------------------------------------------
def get_data_df():
    conn = get_db_connection()
    df = pd.read_sql_query(f"SELECT * FROM air_quality", conn)
    conn.close()
    return df
# end of get_data_df() -----------------------------------------------------------------------

# checks --------------------------------------------------------------
def db_checks(db_path):
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}.")
        time.sleep(2)
        create_db()
    return True
# ------------------------------------------------------------------
