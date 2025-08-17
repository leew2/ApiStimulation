# Unit test for join function in tranform.py
import unittest
import pandas as pd
from tranform import join, average_duplicates

class TestTransform(unittest.TestCase):
	def setUp(self):
		self.df = pd.DataFrame({
			'station_id': ['ST001', 'ST001', 'ST002', 'ST002', 'ST003'],
			'date': ['2023-08-01', '2023-08-02', '2023-08-01', '2023-08-03', '2023-08-01'],
			'aqi': [50, 60, 70, 80, 90],
			'co2_ppm': [400, 410, 420, 430, 440]
		})

	def test_join(self):
		local_df = self.df.iloc[:3]
		db_df = self.df.iloc[2:]
		merged = join(local_df, db_df)
		self.assertIn('station_id', merged.columns)
		self.assertIn('aqi_local', merged.columns)
		self.assertIn('aqi_db', merged.columns)

	def test_average_duplicates(self):
		avg = average_duplicates(self.df)
		self.assertEqual(len(avg), 3)
		st001 = avg[avg['station_id'] == 'ST001']
		self.assertAlmostEqual(st001['aqi'].values[0], 55)
		self.assertAlmostEqual(st001['co2_ppm'].values[0], 405)

if __name__ == "__main__":
	result = unittest.main(exit=False)
	if result.result.wasSuccessful():
		print("pass")

