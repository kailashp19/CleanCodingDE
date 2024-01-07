Feature: Transform data and verify it

  Scenario: Check if the CSV file exists
    Given the transformed file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/GSOD_DATA_TRANSFORMED.csv"
    Then the transformed CSV file should exist

  Scenario: Check length of the "FRSHTT" column
    Given the transformed file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/GSOD_DATA_TRANSFORMED.csv"
    When reading the transformed CSV file
    Then the "FRSHTT" column should not have a fixed length of 6