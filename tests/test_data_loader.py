import unittest
import requests
import sys
sys.path.insert(0, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src")
import data_loader
import os
from datetime import datetime
import config


class TestDataLoader(unittest.TestCase):
    
    def test_api_call(self):
        response = requests.get(base_url)
        self.assertEqual(response.status_code, 200, 'API did return 200')
        self.assertTrue(data_loader.download_file(base_url, landing_path), "API call return did not response")
    
    def test_matching_count(self):
        current_year = datetime.now().year
        expected_count = num_files*(current_year - 1929)
        actual_files_count = 0
        for path, subdirs, files in os.walk(landing_path):
            actual_files_count+=len(files)
        self.assertEqual(expected_count+num_files, actual_files_count)    

if __name__ == "__main__":
    num_files = config.NUM_FILES
    base_url = config.BASE_URL
    landing_path = config.RAW_FOLDER_PATH
    unittest.main(argv=[''], exit=False)