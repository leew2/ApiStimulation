
# Unit test for join function in tranform.py
import unittest
import pandas as pd
from tranform import join

class TestTransform(unittest.TestCase):
	def test_join(self):
		local_df = pd.DataFrame({
			'station_id': ['ST001', 'ST002', 'ST003'],
			'date': ['2023-08-01', '2023-08-02', '2023-08-03'],
			'aqi': [50, 60, 70],
			'co2_ppm': [400, 410, 420]
		})
		db_df = pd.DataFrame({
			'station_id': ['ST001', 'ST002', 'ST004'],
			'date': ['2023-08-01', '2023-08-02', '2023-08-04'],
			'aqi': [55, 65, 75],
			'co2_ppm': [405, 415, 425]
		})
		merged = join(local_df, db_df)
		# Only ST001 and ST002 should match
		self.assertEqual(len(merged), 2)
		self.assertIn('station_id', merged.columns)
		self.assertIn('aqi_local', merged.columns)
		self.assertIn('aqi_db', merged.columns)
		# Check values for ST001
		row = merged[merged['station_id'] == 'ST001'].iloc[0]
		self.assertEqual(row['aqi_local'], 50)
		self.assertEqual(row['aqi_db'], 55)

if __name__ == "__main__":
	result = unittest.main(exit=False)
	if result.result.wasSuccessful():
		print("pass")

