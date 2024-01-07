import pandas as pd
from behave import given, when, then
from datetime import datetime
import sys
sys.path.insert(0, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src")
import config

csv_file_path = config.SAVE_PATH
csv_file_name = config.SAVED_CSV_FILE
file_path = f"{csv_file_path}{csv_file_path}"
exp_num_cols = config.NUM_COLS

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

@given('the file path is "{path}"')
def step_given_file_path(context, path):
    context.file_path = path

@when('reading the CSV file')
def step_when_reading_csv(context):
    context.gsod_data = pd.read_csv(context.file_path)

@then('the number of columns should be {num_cols:d}')
def step_then_num_cols(context, num_cols):
    num_cols = int(num_cols)
    assert len(context.gsod_data.columns) == exp_num_cols, 'Number of columns did not match'

@then('there should be no null values')
def step_then_no_null_values(context):
    assert context.gsod_data.isnull().values.sum() == 0, 'There are null values in the dataset'

@then('the "{column}" column should be of date type')
def step_then_date_column(context, column):
    assert is_date_column(context.gsod_data[column]), f'{column} is not of date type'

@then('the "{column}" column should not contain other than zero and one digits')
def step_then_no_other_digits(context, column):
    context.gsod_data[column] = context.gsod_data[column].astype(str)
    assert not contains_other_digits(context.gsod_data[column]), f'{column} contains other than zero and one digits'
