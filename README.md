# Air Quality Data Processing Project

This project demonstrates how to fetch, clean, merge, and analyze air quality data from both a local CSV and a SQLite database. It includes data transformation, KPI calculation, and saving results to CSV files.

## Features
- Generate synthetic air quality data (local CSV)
- Fetch data from a SQLite database
- Clean and merge datasets
- Calculate KPIs (average AQI, CO₂, etc.)
- Save joined and non-joined data
- Unit tests for transformation logic

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Usage
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```
   python src/main.py
   ```
3. Run tests:
   ```
   python src/test_transform.py
   ```

## File Structure
- `src/main.py` - Main workflow
- `src/fetch_api.py` - Data fetching and API simulation
- `src/tranform.py` - Data transformation and KPI calculation
- `src/test_transform.py` - Unit tests
- `data/` - Generated and processed data files

## Author
Wang L.
Generated with GitHub Copilot
