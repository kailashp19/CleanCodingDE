import data_loader
import data_cleaner
import data_transformer
import config
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #fn used to configure the default behaviour of the logging system.assigned to basic config here. (start logging imdly)
logger = logging.getLogger(__name__)

"""
Author: Kailash Patel
    
Date Created: 2 January, 2023
    
Summary:
The main program to run the ETL pipeline.
"""

def run_pipeline():
    # Defining the variables required to run the pipelines
    file_path = config.RAW_FOLDER_PATH
    save_path = config.SAVE_PATH
    save_file = config.SAVED_CSV_FILE
    transformed_csv_file = config.TRANSFORMED_CSV_FILE
    
    # calling data loader module
    data_loader.download_files_parallel()
    
    # calling data cleaner module and finally saving in processed folder
    gsod_data = data_cleaner.read_gsod_gzip(file_path)
    gsod_data.to_csv(f"{save_path}{save_file}")
    logger.info(f"File is created and saved at {save_path} folder")
    
    # calling data transformer module and finally saving it in processed folder
    trans_df = data_transformer.transform_data(f"{save_path}{save_file}")
    trans_df.to_csv(f"{save_path}{transformed_csv_file}", index=False)
    logger.info(f"File is transformed and saved at {save_path} folder")
    
if __name__ == "__main__":
    run_pipeline()