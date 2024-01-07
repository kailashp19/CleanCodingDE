import pandas as pd
from behave import given, then
import os
import sys
sys.path.insert(0, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src")
import config

save_path = config.SAVE_PATH
save_file = config.TRANSFORMED_CSV_FILE
file_path = f"{save_path}{save_file}"

def has_fixed_length(column, length):
    return all(len(str(value)) == length for value in column)

@given('the transformed file path is "{path}"')
def step_given_file_path(context, path):
    context.file_path = path

@then('the transformed CSV file should exist')
def step_then_csv_file_exists(context):
    assert os.path.exists(context.file_path), f"CSV file {context.file_path} does not exist"

@when('reading the transformed CSV file')
def step_when_reading_csv(context):
    context.transformed_data = pd.read_csv(context.file_path)

@then('the "{column}" column should not have a fixed length of {length:d}')
def step_then_check_column_length(context, column, length):
    column_length = int(length)
    assert not has_fixed_length(context.transformed_data[column], column_length), f'{column} has a fixed length of {length}'