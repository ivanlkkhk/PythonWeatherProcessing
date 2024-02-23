#################################################################
# Description: Project - Part 2 - Database
# Author: Kwok Keung Lai
# Date: Oct 15, 2023
# Usage: This module create a database with using SQLite database.
#        This database will be used to store the weather information
#        sracped in scrape_weather.py and also implement the
#        fetch, save and purge function.
#################################################################
""" This module create a database with using SQLite database.
    This database will be used to store the weather information
    sracped in scrape_weather.py and also implement the
    fetch, save and purge function."""
from dbcm import DBCM  # Import the DBCM context manager from dbcm.py

class DBOperations:
    """This class handled all database related functions. Other
    modules/functions requrie talk to database are require to talk
    throught this class.
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        """
        Create the database and the required table if it doesn't already exist.
        """
        try:
            with DBCM(self.db_name) as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS weather_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sample_date TEXT UNIQUE,
                        location TEXT,
                        min_temp REAL,
                        max_temp REAL,
                        avg_temp REAL
                    )
                ''')
        except Exception as init_error:
            print(f"Error initializing database: {init_error}")

    def save_data(self, weather):
        """
        Save new data to the database, avoiding duplicates.
        Args:
            weather: A list of dictionaries containing weather data.
        """
        location = 'Winnipeg, MB'
        if weather and location:
            try:
                with DBCM(self.db_name) as cursor:
                    sql = """INSERT OR IGNORE INTO weather_data
                            (sample_date, location, min_temp, max_temp, avg_temp)
                            VALUES (?, ?, ?, ?, ?)"""
                    cursor_data = [(date, location,
                                    daily_temps['Min'], daily_temps['Max'], daily_temps['Mean'])
                            for date, daily_temps in weather.items()]
                    cursor.executemany(sql, cursor_data)
            except Exception as save_error:
                print(f"Error saving data to the database: {save_error}")

    def purge_data(self):
        """
        Delete all data from the database.
        """
        try:
            with DBCM(self.db_name) as cursor:
                cursor.execute('DELETE FROM weather_data')
        except Exception as purge_error:
            print(f"Error purging data from the database: {purge_error}")

    def fetch_data(self):
        """
        Retrieve data for plotting.
        Returns:
            A list of tuples containing DB records.
        """
        weather_data = {}
        try:
            with DBCM(self.db_name) as cursor:
                query = 'SELECT '\
                        'sample_date, location, min_temp, max_temp, avg_temp '\
                        'FROM weather_data'
                cursor_data = cursor.execute(query)
                weather_data = {row[0]: {"Min": row[2], "Max": row[3], "Mean": row[4]}
                                for row in cursor_data}
                return weather_data
        except Exception as fetch_error:
            print(f"Error fetching data from the database: {fetch_error}")
            return weather_data

    def get_lastest_date(self):
        """
        Retrieve the lastest date of weather data.
        Returns:
            Latest weather date
        """
        latest_weather_date = ""
        try:
            with DBCM(self.db_name) as cursor:
                query = 'SELECT max(sample_date) FROM weather_data'
                cursor.execute(query)
                latest_weather_date = cursor.fetchone()[0]
                return latest_weather_date
        except Exception as latest_date_error:
            print(f"Error retrieving the latest date: {latest_date_error}")
            return latest_weather_date
