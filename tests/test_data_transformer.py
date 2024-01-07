import unittest
import sys
sys.path.insert(2, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src/")
import pandas as pd
import config
import os


def has_fixed_length(column, length):
    return all(len(str(value)) == length for value in column)


class TestDataTransformer(unittest.TestCase):
    
    def test_if_csv_file_exists(self):
        self.assertTrue(os.path.exists(file_path), f"CSV file {file_path} exists")
        
    def test_frshtt_len(self):
        transformed_data = pd.read_csv(file_path)
        column_to_check = 'FRSHTT'
        fixed_length = 6
        self.assertFalse(has_fixed_length(transformed_data[column_to_check], fixed_length))


if __name__ == "__main__":
    exp_num_cols = config.NUM_COLS
    processed_path = config.SAVE_PATH
    t_csv_file = config.TRANSFORMED_CSV_FILE
    file_path = f"{processed_path}{t_csv_file}"
    unittest.main(argv=[''], exit=False)