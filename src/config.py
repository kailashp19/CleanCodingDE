from datetime import date
from dateutil.relativedelta import relativedelta

BASE_URL = "https://www1.ncdc.noaa.gov/pub/data/gsod/"
RAW_FOLDER_PATH = "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/raw/"
NUM_FILES = 10
INCREMENTAL = True
PREVIOUS_DATE = date.today() - relativedelta(days=1)
COLUMN_NAMES = [
        "station_id", "WBAN", "date", "temperature", "temperature_count",
        "dew_point", "dew_point_count", "sea_level_pressure",
        "sea_level_pressure_count",
        "station_pressure", "station_pressure_count", "visibility",
        "visibility_count",
        "wind_speed", "wind_speed_count", "max_wind_speed", "GUST",
        "MAX", "MIN", "PRCP", "SNDP", "FRSHTT"
    ]
SAVE_PATH = "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/data/processed/"
SAVED_CSV_FILE = "gsod_data.csv"
TRANSFORMED_CSV_FILE = "GSOD_DATA_TRANSFORMED.csv"
NUM_COLS = 23
LOGGING_FILE_PATH = "C:/Users/sg1389-dsk05-user1/Kailash_Patel_CleanCoding/weather_data_analysis/weather_data_pipeline_KP/Logs/data.log"
