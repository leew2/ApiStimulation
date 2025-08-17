import pandas as pd
import os
# Combine 2 data from CSV and DB into one
# Clean Both CSV and DB
# Combine and Sort them
# Calculate New KPIs like AQI deltas, CO₂ reductions

def handler(local_df, db_df):
    merged = combine_data(local_df, db_df)
    print(f"Combined data size: {merged.shape}")
    kpi_df = average_duplicates(merged)
    save_kpis(kpi_df.sort_values(by='station_id'), "kpis")
    print(f"merged KPI: {kpi_df.shape}" )
    joined = join(local_df, db_df)
    return joined

def save_kpis(kpi_df, name='kpis'):
    """
    Save the KPI DataFrame to a CSV file in the 'data' folder.
    """
    os.makedirs("data", exist_ok=True)
    kpi_df.to_csv(os.path.join("data", f"{name}.csv"), index=False)
    print(f"KPIs saved to data/kpi_{name}.csv")

# Transform functions ---------------------------------------------------
# combine ---------------------------------------------------
def average_duplicates(df):
    # Find AQI and CO2 columns
    aqi_cols = [col for col in df.columns if 'aqi' in col]
    co2_cols = [col for col in df.columns if 'co2' in col]
    # Group by station_id and average the AQI and CO2 columns
    grouped = df.groupby('station_id')[aqi_cols + co2_cols].mean().reset_index()
    return grouped
# Combine local and db data vertically
def combine_data(local_df, db_df):
    combined = pd.concat([local_df, db_df], ignore_index=True)
    return combined
# combine -----------------------------------------------------------------------


# joined -------------------------------------------------------------------------
# Calculate average AQI and CO2 for each station_id
def calculate_kpis(df):
    # Find all AQI and CO2 columns
    aqi_cols = [col for col in df.columns if 'aqi' in col]
    co2_cols = [col for col in df.columns if 'co2' in col]
    # Calculate row-wise mean for AQI and CO2
    df['avg_aqi'] = df[aqi_cols].mean(axis=1)
    df['avg_co2'] = df[co2_cols].mean(axis=1)
    return df[['station_id', 'avg_aqi', 'avg_co2']]



def join(local_df, db_df, on="station_id"):
    local_df = check_data(local_df)
    db_df = check_data(db_df)

    merged = pd.merge(local_df, db_df, on=on, how='right', suffixes=('_local', '_db'))
    return merged
# joined ---------------------------------------------------------------------------------------

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


