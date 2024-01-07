import requests
from behave import given, when, then
from datetime import datetime
import os
import sys
sys.path.insert(0, "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/src")
import data_loader
import config

base_url = config.BASE_URL
landing_path = config.RAW_FOLDER_PATH
num_files = config.NUM_FILES

@given('I have entered the {url} in the search bar')
def step_given_base_url(context, url):
    context.base_url = url

@when('I hit submit button')
def step_when_api_called(context):
    context.response = requests.get(context.base_url)

@then('the response status code should be 200')
def step_then_response_status(context):
    assert context.response.status_code == 200, 'API did not return 200'

@then('the API should download a file to the landing path')
def step_then_api_download_file(context):
    assert data_loader.download_file(context.base_url, landing_path), 'API call did not download a file'

@given('the landing path is "{path}"')
def step_given_landing_path(context, path):
    context.landing_path = path

@when('counting the actual files')
def step_when_counting_files(context):
    context.actual_files_count = 0
    for path, subdirs, files in os.walk(context.landing_path):
        context.actual_files_count += len(files)

@then('the actual files count should match the expected count')
def step_then_matching_count(context):
    current_year = datetime.now().year
    expected_count = num_files * (current_year - 1929)
    assert context.actual_files_count == expected_count + num_files, 'Actual files count matched expected count'
