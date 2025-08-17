

# Combine 2 data from CSV and DB into one
# Clean Both CSV and DB
# Combine and Sort them
# Calculate New KPIs like AQI deltas, CO₂ reductions
import pandas as pd

def join(local_df, db_df, on="station_id"):
    local_df = check_data(local_df).dropna()
    db_df = check_data(db_df).dropna()

    merged = pd.merge(local_df, db_df, on=on, suffixes=('_local', '_db'))
    return merged

# Check if input is a DataFrame, if not convert to DataFrame and return
def check_data(data):
    if isinstance(data, pd.DataFrame):
        print("Input is a pandas DataFrame.")
        return data
    else:
        print("Input is NOT a pandas DataFrame. Attempting to convert...")
        try:
            df = pd.DataFrame(data)
            print("Conversion successful.")
            return df
        except Exception as e:
            print(f"Conversion failed: {e}")
            return None


