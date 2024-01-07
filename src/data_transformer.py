import pandas as pd
import config
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #fn used to configure the default behaviour of the logging system.assigned to basic config here. (start logging imdly)
logger = logging.getLogger(__name__)

"""
Author: Kailash Patel
    
Date Created: 2 January, 2023
    
Summary:
This program picks the cleaned CSV file
and transform it into suitable format for further analysis.
"""


# Define a function to map the positions of '1' to the respective weather types
def weather_type(row):
    """
    A helper function to assign the weather type
    on the binary data

    Args:
        row (int): A column containing binary type data

    Returns:
        string: containing the wather type 
    """
    conditions = ['Fog', 'Rain', 'Snow', 'Hail', 'Thunder', 'Tornado']
    result = None
    for i in range(5, -1, -1):
        if row // (10 ** i) % 10 == 1:
            result = conditions[i]
            break
    return result if result else 'No Weather'

def transform_data(csv_file):
    """
    A function to transform the data to a suitable format.

    Args:
        csv_file (string): A file contianing the data in CSV format.
    Returns:
        dataframe: A dataframe containing cleaned data
    """
    try:
        cleaned_df = pd.read_csv(csv_file)
        
        # Step 1: Replace missing values (9999.9) with NaN
        cleaned_df = cleaned_df.replace(to_replace=[9999.9, 99.9, 999.9], value=np.nan)
        
        # Step 2: Convert PRCP column to numeric, handling 'G' suffix
        cleaned_df['PRCP'] = pd.to_numeric(cleaned_df['PRCP'].str.rstrip('G'), errors='coerce')
        
        # Step 3: Convert date column to datetime
        cleaned_df['date'] = cleaned_df['date'].apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))
        
        # Step 4: Handle outliers or incorrect values based on domain knowledge
        # For example, if a temperature of 999.9 is unrealistic, replace it with NaN
        # Assuming temperature values should be within a reasonable range
        temperature_threshold = (-70.0, 70.0)
        cleaned_df['temperature'] = cleaned_df['temperature'].apply(lambda x: x if temperature_threshold[0] <= x <= temperature_threshold[1] else pd.NA)
        
        # Step 5: Handle categorical data (if any)
        # For example, convert 'FRSHTT' into separate binary columns for each flag
        cleaned_df['weather_type'] = cleaned_df['FRSHTT'].apply(weather_type)
        return cleaned_df
    except IOError as ie:
        logger.error(f"Error while reading the file: {ie}")
        raise
    except TypeError as te:
        logger.error(f"Type Error occured: {te}")
        raise
    except KeyError as ke:
        logger.error(f"Specified key not found: {ke}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occured: {e}")
        raise

    
if __name__ == "__main__":
    # Testing
    save_path = config.SAVE_PATH
    save_file = config.SAVED_CSV_FILE
    transformed_csv_file = config.TRANSFORMED_CSV_FILE
    cdf = transform_data(f"{save_path}{save_file}")