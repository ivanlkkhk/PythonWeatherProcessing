#################################################################
# Description: Project - Part 4 - User Interaction
# Author: Kwok Keung Lai
# Date: Oct 23, 2023
# Usage: This module used generate the user menu for user pick up
#        the function they want to use, and this modeule will
#        integrate functions I have created in previous parts.
#################################################################
"""Main module for initiate the main menu and interact with
   other modules."""
from menu import Menu
from db_operations import DBOperations
from scrape_weather import WeatherScraper
from plot_operations import PlotOperations

class WeatherProcessor:
    """ Main system class to consturct the system menu and
        and interact with other modules.
    """
    def __init__(self):
        """ Constructor for initiate the main menu. """
        self.main_menu = Menu(
            title="Weather Data Processor Menu:",
            options=[
                ("Download a latest weather data", self.download_weather_data),
                ("Generate a box plot", self.generate_box_plot),
                ("Generate a line plot", self.generate_line_plot),
                ("Purge data from the database", self.purge_data),
                ("Quit", Menu.CLOSE),
            ],
            
            prompt="Enter your choice: "
        )

    def run(self):
        """ This function is used to open the main menu."""
        self.main_menu.open()


    def download_weather_data(self):
        """ Function for download the latest weather data and update into database."""
        weather_db = DBOperations("weather_data")
        scraper = WeatherScraper()

        weather_data = scraper.scrape_weather(weather_db.get_lastest_date())

        if weather_data:
            weather_db.save_data(weather_data)
            print("Weather data has been downloaded and saved to the database.")
        else:
            print("Failed to download weather data.")
        input("Press Enter to continue...")

    def generate_box_plot(self):
        """ Function for generate the box plot. """
        from_year, to_year = self.input_year_range()
        if from_year and to_year:
            weather_db = DBOperations("weather_data")
            weather_data = weather_db.fetch_data()
            if weather_data:
                plotter = PlotOperations(weather_data)
                plotter.create_boxplot(from_year, to_year)

    def generate_line_plot(self):
        """ Function for generate the line plot. """
        selected_year, selected_month = self.input_year_month()
        if selected_year and selected_month:
            weather_db = DBOperations("weather_data")
            weather_data = weather_db.fetch_data()
            if weather_data:
                plotter = PlotOperations(weather_data)
                plotter.create_lineplot(str(selected_year), str(selected_month))

    def purge_data(self):
        """ After user selected the purge database option from the menu, 
        this is the question to confirm to purge data from the database."""
        confirm = input("Are you sure you want to purge all data from the database? (Y/N): ")
        if confirm.lower() == 'y':
            weather_db = DBOperations("weather_data")
            weather_db.purge_data()
            print("Database has been purged.")
        else:
            print("No data was purged.")
        input("Press Enter to continue...")


    def input_year_range(self):
        """ Requesting user enter the range of the years for pass into the function for 
        filtering use."""
        min_year = 1900
        max_year = 2100
        from_year = input("Enter the starting year: ")
        to_year = input("Enter the ending year: ")
        if not from_year.isdigit() or not to_year.isdigit() or int(from_year) > int(to_year):
            print("Invalid input. Please enter valid years.")
            input("Press Enter to continue...")
            return None, None
        if int(from_year) < min_year or int(to_year) > max_year:
            print(f"Year should be between {min_year} and {max_year}.")
            input("Press Enter to continue...")
            return None, None
        return int(from_year), int(to_year)

    def input_year_month(self):
        """ Requesting user enter the years and month for pass into the function for 
        filtering use."""
        min_year = 1900
        max_year = 2100
        selected_year = input("Enter the year: ")
        selected_month = input("Enter the month (1-12): ")
        if not selected_year.isdigit() or \
            not selected_month.isdigit() or \
            int(selected_month) < 1 or \
            int(selected_month) > 12:
            print("Invalid input. Please enter a valid year and month.")
            input("Press Enter to continue...")
            return None, None
        if int(selected_year) < min_year or int(selected_year) > max_year:
            print(f"Year should be between {min_year} and {max_year}.")
            input("Press Enter to continue...")
            return None, None
        return int(selected_year), int(selected_month)

if __name__ == "__main__":
    processor = WeatherProcessor()
    processor.run()
