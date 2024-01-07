import pandas as pd
import config
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #fn used to configure the default behaviour of the logging system.assigned to basic config here. (start logging imdly)
logger = logging.getLogger(__name__)

"""
Author: Kailash Patel
    
Date Created: 2 January, 2023
    
Summary:
This program creates an informative visuals
"""

def temp_and_weather_type_plot(csv_file):

    try:

        # Reading the transformed data in a dataframe
        transformed_data = pd.read_csv(csv_file)

        # Plotting
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

        # Bar plot for weather_type
        transformed_data['weather_type'].value_counts()\
            .plot(kind='bar', ax=axes[0], color='green')
        axes[0].set_title('Weather Type Distribution')
        axes[0].set_xlabel('Weather Type')
        axes[0].set_ylabel('Count')

        # Line plot for Temperature
        transformed_data.plot(x='weather_type',
                              y='temperature',
                              kind='line',
                              marker='o',
                              ax=axes[1],
                              color='skyblue')
        axes[1].set_title('Temperature by Weather Type')
        axes[1].set_xlabel('Weather Type')
        axes[1].set_ylabel('Temperature (°C)')

        plt.tight_layout()
        plt.show()
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

def avg_temp_plot(csv_file):

    try:

        # Reading the transformed data in a dataframe
        transformed_data = pd.read_csv(csv_file)

        # Convert the 'date' column to datetime format
        transformed_data['date'] = pd.to_datetime(transformed_data['date'])

        # Extract the year from the 'date' column and create a new column 'year'
        transformed_data['year'] = transformed_data['date'].dt.year
        
        # Extract the month from the 'date' column and create a new column 'month'
        transformed_data['month'] = transformed_data['date'].dt.month

        # Group the data by month and calculate the average temperature for each month
        average_temp_month = transformed_data.groupby('month')['temperature'].mean()

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(average_temp_month.index, average_temp_month, marker='o', linestyle='-', color='b')
        plt.title('Average Temperature by Month')
        plt.xlabel('Month')
        plt.ylabel('Average Temperature')
        plt.grid(True)
        plt.show()
        
        # Group the data by month and calculate the average temperature for each month
        average_temp_year = transformed_data.groupby('year')['temperature'].mean()

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(average_temp_year.index, average_temp_year, marker='o', linestyle='-', color='b')
        plt.title('Average Temperature by Year')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.grid(True)
        plt.show()
    except IOError as ie:
        logger.error(f"Error while reading the file: {ie}")
    except TypeError as te:
        logger.error(f"Type Error occured: {te}")
    except KeyError as ke:
        logger.error(f"Specified key not found: {ke}")
    except Exception as e:
        logger.error(f"An unexpected error occured: {e}")


if __name__ == "__main__":
    save_path = config.SAVE_PATH
    t_csv_file = config.TRANSFORMED_CSV_FILE
    temp_and_weather_type_plot(f"{save_path}{t_csv_file}")
    avg_temp_plot(f"{save_path}{t_csv_file}")
