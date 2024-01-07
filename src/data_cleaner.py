import pandas as pd
import os
import config
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #fn used to configure the default behaviour of the logging system.assigned to basic config here. (start logging imdly)
logger = logging.getLogger(__name__)

"""
Author: Kailash Patel
    
Date Created: 2 January, 2023
    
Summary:
This program picks all the gzip files saved
in raw folder and read the contents of the file
in a dataframe and finally saves it in processed folder.
"""

def read_gsod_gzip(file_path):
    """A function to read the content of downloaded GSIP file
    and save it in a dataframe

    Args:
        file_path string: Actual path of the gzip data files

    Returns:
        a dataframe: combined dataframe for all the data
        read from GZIP file
    """
    try:
        # creating an empty dataframe to hold all the dataframes
        combined_df = pd.DataFrame()
        for path, subdirs, files in os.walk(file_path):
            for name in files:
            
                # Read gzip file and create Pandas DataFrame
                csv_file_2 = os.path.join(path, name)
                with open(csv_file_2, 'rt') as f:
                    df = pd.read_csv(f, 
                                    header=None, 
                                    names=config.COLUMN_NAMES, 
                                    delim_whitespace=True, 
                                    skiprows=1, 
                                    dtype={'station_id': str, 'FRSHTT': str}
                                    )
                    logger.info(f"Successfully read the file {csv_file_2}")
                    combined_df = pd.concat([combined_df, df])
        return combined_df
    except IOError as ie:
        logger.error(f"An error occurred while accessing the folder {csv_file_2}: {ie}")
        raise
    except KeyError as ke:
        logger.error(f"A key error occured: {ke}")
        raise
    except ValueError as ve:
        logger.error(f"A value error has occurred: {ve}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    # Testing
    file_path = config.RAW_FOLDER_PATH
    gsod_data = read_gsod_gzip(file_path)

