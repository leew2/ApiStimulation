
import os
import random
import pandas as pd
from fetch_api import api
from faker import Faker
from tranform import handler

def main():
    local_data("check_local")
    data = {
        "station_id": "ST001",
        "date": "2023-08-01",
        "aqi": 1,
        "co2_ppm": 1
    }

    api.POST(data)
    db = api.GET()
    local = local_data("get_local")

    aqi, co2 = handler(local, db)
    api.DELETE(data)
    print(f"database Data: {api.GET()}")
    print(f"local Data: {local}")
    print(f"Overall Average AQI: {aqi}, Overall Average CO2: {co2}")

# Create local synthetic data -----------------------------------------------------------------------------

def local_data(task = None):
    csv_path = "data/weather_station_data.csv"
    if task == "check_local":
        if not os.path.exists(csv_path):
            print(f"{csv_path} not found. Creating local data...")
            create_local_data()
        else:
            print(f"{csv_path} already exists.")
    elif task == "get_local":
        return pd.read_csv(csv_path)

def create_local_data():
    fake = Faker()
    data = []
    for _ in range(100):
        entry = {
            "station_id": fake.bothify("ST###"),
            "date": fake.date_between("-30d", "today").isoformat(),
            "aqi": random.randint(10, 200),
            "co2_ppm": round(random.uniform(350, 450), 1)
        }
        data.append(entry)
    df = pd.DataFrame(data)
    if not os.path.exists("data"):
        os.makedirs("data", exist_ok=True)
    csv_path = "data/weather_station_data.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Data saved to {csv_path}")
    return csv_path
# end of create_local_data() -----------------------------------------------------------------



if __name__ == "__main__":
    main()
    print("Created with Copilot")
