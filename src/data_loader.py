import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from urllib.parse import urljoin
import config
import gzip
from io import BytesIO
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #fn used to configure the default behaviour of the logging system.assigned to basic config here. (start logging imdly)
logger = logging.getLogger(__name__)
"""
Author: Kailash Patel
    
Date Created: 25 December, 2023
    
Summary:
This File hits the main GSOD URL https://www1.ncdc.noaa.gov/pub/data/gsod/,
goes to each folder and picks 10 files from each folder. It also checks
if there is any file updated then it only picks the new file from
the respective folder.
Finally it saves the file the raw folder.
"""


# Function to download a file
def download_file(url, destination):
    """Helper function to retrieve the GSOD data
    and save it in destination folder 

    Args:
        url (String): URL for the respective year
        destination (String): A file path to save the files

    Returns:
        response (String): The content of URL 
    """
    try:
        response = requests.get(url)
        return response.content
    except requests.exceptions.RequestException as e:
        logger(f"Error occurred while calling the {url}: {e}")


# Function to download files from a specific year folder
def download_files_from_year(year_folder):
    """Helper function to retrieve the GSOD data
    for the particular year

    Args:
        year_folder (String): year number

    Returns:
        None: Saves the binary file in destination folder
    """
    try:
        year_url = urljoin(base_url, year_folder)
        response = requests.get(year_url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Extract links to files
        file_links = [a['href'] for a in soup.find_all('a') 
                    if a['href'].endswith('.op.gz')]
    
        # Check if the folder is modified in the last day for incremental load
        if incremental:
            last_modified_element = soup.find_all('td', align='right')
            last_modified_date = last_modified_element[-2].get_text(strip=True)
            last_modified_date = datetime.strptime(last_modified_date, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d')
            yesterday = datetime.now().date() - timedelta(days=1)
            yesterday = yesterday.strftime('%Y-%m-%d')
            if last_modified_date < yesterday:
                logger.info(f"Skipping {year_folder} - No updates in the last day.")
                return
    
        # Download only the specified number of files
        file_links = file_links[:num_files]
    
        # Download files
        destination_folder = os.path.join(raw_folder_path, year_folder)
        os.makedirs(destination_folder, exist_ok=True)
    
        for file_link in file_links:
            file_url = year_url + '/' + file_link
            file_name = os.path.basename(file_link)
            destination_path = os.path.join(destination_folder,
                                        file_name.replace('.op.gz',
                                                          '.op'))
            logger.info(f"Downloading {file_url} to {destination_path}")
        
            # Download and decompress the file
            file_content = download_file(file_url, destination_path)
            with gzip.GzipFile(fileobj=BytesIO(file_content), mode='rb') as gz_file:
                decompressed_content = gz_file.read()
            
            # Save the decompressed content to a new file
            with open(destination_path, 'wb') as output_file:
                output_file.write(decompressed_content)
    except IOError as ie:
        logger.error(f"Error accessign the folder {year_folder}: {ie}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise


# Combined function to download files for each year in parallel
def download_files_parallel():
    """Function to download the files parallely using Threadpools
    """
    try:
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Extract links to year folders
            response = requests.get(base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            year_folders = [a['href'] for a in soup.find_all('a') if a['href']]
            year_values = [value.replace('/', '') for value in year_folders 
                        if value.replace('/', '').isdigit()]
        
            # Download files for each year in parallel
            partial_download = lambda year: download_files_from_year(year)
            executor.map(partial_download, year_values)
    except Exception as e:
        logger.error(f"An unexpected error occured for Thread Pool Executor: {e}")
        raise


if __name__ == "__main__":
    
    # Defining the variables from config file
    base_url = config.BASE_URL
    raw_folder_path = config.RAW_FOLDER_PATH
    num_files = config.NUM_FILES
    incremental = config.INCREMENTAL
    
    # calling the download_files_parallel to download the files parallely
    download_files_parallel()