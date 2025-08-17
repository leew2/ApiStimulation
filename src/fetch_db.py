import random
import sqlite3
from faker import Faker
import pandas as pd

# Get a connection to the database ----------------------------------------------------
def get_db_connection():
	"""Connect to the env.db SQLite database in the data folder and return the connection object."""
	db_path = "./data/env.db"
	conn = sqlite3.connect(db_path)
	return conn
# end of get_db_connection() ---------------------------------------------------

# Create the database and populate it with synthetic data -----------------------
def create_db():
    fake = Faker()
    rows = []
    for _ in range(500):
        rows.append({
            "station_id": fake.bothify("ST###"),
            "date": fake.date_between("-30d", "today"),
            "aqi": random.randint(10, 200),
            "co2_ppm": round(random.uniform(350, 450), 1)
        })

    df = pd.DataFrame(rows)
    con = sqlite3.connect("data/env.db")
    df.to_sql("air_quality", con, if_exists="replace", index=False)
    con.close()
    print("✅ synthetic database saved to data/env.db")
# end of create_db() -----------------------------------------------------------------------


