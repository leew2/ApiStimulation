# Air Quality Data Processing Project

This project demonstrates how to fetch, clean, merge, and analyze air quality data from both a local CSV and a SQLite database. It includes data transformation, KPI calculation, logging, and saving results to CSV files.

## Features
- Generate synthetic air quality data (local CSV)
- Fetch data from a SQLite database
- Clean and merge datasets
- Calculate KPIs (average AQI, CO₂, etc.)
- Save joined and non-joined data
- Unit tests for transformation logic
- Logging of all API/database actions (POST, GET, PUT, DELETE, CREATE_DB) to `log/api.log`

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies
- Note: `sqlite3` is included with the Python standard library and does not need to be installed via pip.

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
- `src/fetch_api.py` - Data fetching, API simulation, and logging
- `src/fetch_db.py` - Database creation and logging
- `src/tranform.py` - Data transformation and KPI calculation
- `src/test_transform.py` - Unit tests
- `data/` - Generated and processed data files
- `log/` - API and database action logs

## Author
Wang L.
Generated with GitHub Copilot
