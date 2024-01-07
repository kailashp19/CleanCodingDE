Feature: API Call

  Scenario: Verify API call
    Given I have entered the https://www1.ncdc.noaa.gov/pub/data/gsod/ in the search bar
    When I hit submit button
    Then the response status code should be 200
    And the API should download a file to the landing path

  Scenario: Verify matching count
    Given the landing path is "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/raw/"
    When counting the actual files
    Then the actual files count should match the expected count
