#################################################################
# Description: Project - Part 1 - Scraping
# Author: Kwok Keung Lai
# Date: Oct 15, 2023
# Usage: This module create a HTML Parser class to scrape
#        Winnipeg weather data from the Environment Canada website
#################################################################

"""This module create a HTML Parser class to scrape Winnipeg weather 
data from the Environment Canada website"""
import urllib.request
from html.parser import HTMLParser
from datetime import datetime
from dateutil.relativedelta import relativedelta

class WeatherScraper(HTMLParser):
    """
    A class to scrape Winnipeg weather data from the Environment Canada website.
    """

    def __init__(self):
        super().__init__()
        self.in_date = False
        self.in_max_temp = False
        self.in_min_temp = False
        self.in_mean_temp = False
        self.in_dynamic_data_table = False
        self.in_tbody = False
        self.title_date = None
        self.date = None
        self.weather = {}
        self.base_url = "http://climate.weather.gc.ca/climate_data/daily_data_e.html"
        self.current_date = datetime.now().date()
        self.col_count=0

    def fetch_weather_data(self, url):
        """
        Fetch weather data HTML content from the given URL.
        """
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except urllib.error.URLError as url_exception:
            print(f"Error fetching data from {url}: {url_exception}")
            return None

    def handle_starttag(self, tag, attrs):
        """
        Handle the start of an HTML tag.
        """
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'id' and attr[1] == 'dynamicDataTable':
                    # Set a flag to indicate that we're inside the desired <div>.
                    self.in_dynamic_data_table = True

        if self.in_dynamic_data_table:
            if tag == 'tbody' :
                self.in_tbody = True
            if tag == 'abbr' and self.in_tbody:
                for attr in attrs:
                    if attr[0] == 'title' :
                        self.in_date = True
                        self.title_date = attr[1]
            if tag == 'td' and self.in_date:
                self.col_count += 1
                match self.col_count:
                    case 1:
                        self.in_max_temp = True
                    case 2:
                        self.in_min_temp = True
                    case 3:
                        self.in_mean_temp = True

    def handle_data(self, data):
        """
        Handle the data content within an HTML tag.
        """
        if self.in_dynamic_data_table:
            if self.in_date:
                if self.is_valid_date(self.title_date):
                    self.date = datetime.strptime(self.title_date, '%B %d, %Y').date()
            if self.in_max_temp:
                if self.is_float(data):
                    self.weather[self.date.strftime("%Y-%m-%d")] = {"Max": float(data)}
                else:
                    self.weather[self.date.strftime("%Y-%m-%d")] = {"Max": None}
                self.in_max_temp = False
            if self.in_min_temp:
                if self.is_float(data):
                    self.weather[self.date.strftime("%Y-%m-%d")]["Min"] = float(data)
                else:
                    self.weather[self.date.strftime("%Y-%m-%d")]["Min"] = None
                self.in_min_temp = False
            if self.in_mean_temp:
                if self.is_float(data):
                    self.weather[self.date.strftime("%Y-%m-%d")]["Mean"] = float(data)
                else:
                    self.weather[self.date.strftime("%Y-%m-%d")]["Mean"] = None
                self.in_mean_temp = False
                self.reset_flags()

    def reset_flags(self):
        """Reset the parser flags for temperature data."""
        self.in_date = False
        self.col_count = 0

    def scrape_weather(self, latest_date_str=None):
        """
        Scrape weather data from the website and store it in the weather dictionary.
        """
        latest_date = datetime.now().date()
        date_format = "%Y-%m-%d"
        if latest_date_str is not None:
            # Convert the string to a datetime object
            latest_date = datetime.strptime(latest_date_str, date_format).date()
        else:
            latest_date = datetime.strptime("1950-01-01", date_format).date()

        while True:
            if latest_date >= self.current_date:
                break
            url = f"{self.base_url}?StationID=27174&timeframe=2&StartYear=1840" \
                  f"&EndYear={self.current_date.year}&Day=1" \
                  f"&Year={self.current_date.year}&Month={self.current_date.month}#"

            html_data = self.fetch_weather_data(url)

            # Check if the "We're sorry we were unable to satisfy your request."
            # exists (indicating no data)
            if "We're sorry we were unable to satisfy your request." in html_data:
                break

            self.feed(html_data)
            # Subtract one month from the current date
            self.current_date -= relativedelta(months=1)

        return self.weather

    def is_float(self, str_data):
        """ Function for check data is float number."""
        try:
            float(str_data)
            return True
        except ValueError:
            return False

    def is_valid_date(self, date_string):
        """ Function for check data is date string with MMM dd, YYYY format."""
        try:
            datetime.strptime(date_string, '%B %d, %Y')
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    scraper = WeatherScraper()
    weather = scraper.scrape_weather()

    if weather:
        for date, daily_temps in weather.items():
            print(f"{date}: " \
                f"Max={daily_temps['Max']}, " \
                f"Min={daily_temps['Min']}, " \
                f"Mean={daily_temps['Mean']}")
    else:
        print("No weather data retrieved. Check for errors in the script.")

    print(weather)
