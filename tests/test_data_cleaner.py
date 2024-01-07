import unittest
import sys
sys.path.insert(1, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src/")
import pandas as pd
import config
import data_cleaner


def is_date_column(column):
    try:
        pd.to_datetime(column)
        return True
    except ValueError:
        return False

def contains_other_digits(column):
    for value in column:
        for digit in str(value):
            if digit not in ('0', '1'):
                return True
    return False


class TestDataCleaner(unittest.TestCase):
    
    def test_num_cols(self):
        gsod_data = pd.read_csv(file_path)
        num_cols = len(gsod_data.axes[1])
        self.assertEqual(num_cols, exp_num_cols)
    
    def test_nulls_any(self):
        gsod_data = pd.read_csv(file_path)
        is_null_val = gsod_data.isnull().values.sum()
        self.assertEqual(is_null_val, 0)
    
    def test_date_column(self):
        # Test if the column is of date type
        gsod_data = pd.read_csv(file_path)
        column_to_check = 'date'
        self.assertTrue(is_date_column(gsod_data[column_to_check]))
    
    def test_other_zero_one(self):
        # Test if the column is of date type
        gsod_data = pd.read_csv(file_path)
        gsod_data['FRSHTT'] = gsod_data['FRSHTT'].astype(str)
        self.assertFalse(contains_other_digits(gsod_data['FRSHTT']))


if __name__ == "__main__":
    exp_num_cols = config.NUM_COLS
    save_csv_path = config.SAVE_PATH
    saved_csv_file = config.SAVED_CSV_FILE
    file_path = f"{save_csv_path}{saved_csv_file}"
    unittest.main(argv=[''], exit=False)