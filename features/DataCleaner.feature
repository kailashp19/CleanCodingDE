Feature: Clean and Verify Data Integrity

  Scenario: Verify the number of columns
    Given the file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/gsod_data.csv"
    When reading the CSV file
    Then the number of columns should be 23

  Scenario: Verify no null values
    Given the file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/gsod_data.csv"
    When reading the CSV file
    Then there should be no null values

  Scenario: Verify date column
    Given the file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/gsod_data.csv"
    When reading the CSV file
    Then the "date" column should be of date type

  Scenario: Verify absence of other than zero and one digits in the "FRSHTT" column
    Given the file path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/gsod_data.csv"
    When reading the CSV file
    Then the "FRSHTT" column should not contain other than zero and one digits