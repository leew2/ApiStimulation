# imported from assignment
# scripts/generate_fake_data.py
import os
from faker import Faker
from fetch_db import get_db_connection
import pandas as pd
import random
import time
from fetch_db import create_db

# main frame of API --------------------------------------------------------------
def api(target, key):
    # Simulate API call
    time.sleep(1)
    if target == "get_db" and key == "your_api_key":
        if db_checks("./data/env.db"):
            df = get_data_df()
            return {"data": df}
    elif target == "sort_data" and key == "your_api_key":
        if db_checks("./data/env.db"):
            df = get_data_df()
            sorted_df = df.sort_values(by="air_quality", ascending=False)
            return {"data": sorted_df}
    else:
        return {"error": f"Unknown target: {target}"}
# end of api() --------------------------------------------------------------

# create data from db -------------------------------------------------------------------
def get_data_df():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM air_quality", conn)
    conn.close()
    return df
# end of get_data_df() -----------------------------------------------------------------------

# checks --------------------------------------------------------------
def db_checks(db_path):
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}.")
        time.sleep(2)
        create_db()
    data = get_data_df()
    print(data)
    return True
# ------------------------------------------------------------------


# Create local synthetic data -----------------------------------------------------------------------------
def create_local_data():
    fake = Faker()
    data = []
    for _ in range(100):
        entry = {
            "station_id": fake.bothify("ST###"),
            "date": fake.date_between("-30d", "today").isoformat(),
            "air_quality": random.randint(10, 200),
            "co2_ppm": round(random.uniform(350, 450), 1)
        }
        data.append(entry)
    df = pd.DataFrame(data)
    csv_path = "../data/weather_station_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Data saved to {csv_path}")
    return csv_path
# end of create_local_data() -----------------------------------------------------------------


