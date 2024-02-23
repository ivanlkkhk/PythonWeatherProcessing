#################################################################
# Description: Project - Part 3 - Plotting
# Author: Kwok Keung Lai
# Date: Oct 20, 2023
# Usage: This module create a boxplot and a line plot by using
#        matplotlib. The PlotOperation class require to initiate
#        with the weather data, which could be the data get from
#        the database, then it will have functions for plotting.
#################################################################
""" This module create a boxplot and a line plot by using
    matplotlib. The PlotOperation class require to initiate
    with the weather data, which could be the data get from
    the database, then it will have functions for plotting.
"""
import calendar
import matplotlib.pyplot as plt

class PlotOperations:
    """This class will be use for pop up diagrams."""
    def __init__(self, weather_data_arg):
        """Constructor - initiate with weather data."""
        self.weather_data = weather_data_arg

    def create_boxplot(self, start_year, end_year):
        """
        Create a boxplot of mean temperatures for each month within the date range.
        Args:
            start_year (str): The starting year for the date range (e.g., "2000").
            end_year (str): The ending year for the date range (e.g., "2020").
        """
        try:
            # Convert year strings to integers for comparison
            start_year = int(start_year)
            end_year = int(end_year)

            # Filter data based on the date range
            filtered_data = {
                date: daily_temps
                for date, daily_temps in self.weather_data.items()
                    if start_year <= int(date[:4]) <= end_year
            }

            # Extract mean temperatures for each month
            monthly_data = {month: [] for month in range(1, 13)}

            for date, daily_temps in filtered_data.items():
                month = int(date[5:7])  # Extract the month from the date
                mean_temp = daily_temps["Mean"]
                if mean_temp is not None:
                    monthly_data[month].append(mean_temp)

            # Prepare data for boxplot
            data_to_plot = [monthly_data[month] for month in range(1, 13)]

            # Create and display the boxplot
            plt.boxplot(data_to_plot)
            plt.xticks(range(1, 13), [str(month) for month in range(1, 13)])
            plt.xlabel("Month")
            plt.ylabel("Mean Temperature (°C)")
            plt.title(f"Mean Temperatures by Month ({start_year} to {end_year})")
            plt.show()
        except Exception as boxplot_error:
            print(f"Error creating boxplot: {boxplot_error}")

    def create_lineplot(self, year, month):
        """
        Create a line plot of daily mean temperatures for a specific year and month.
        Args:
            year (str): The year to plot data for (e.g., "2020").
            month (str): The month to plot data for (e.g., "1").
        """
        try:
            year_month = f"{year}-{month.zfill(2)}" # Convert year and month to "YYYY-MM" format
            self.create_lineplot_by_date(year_month)
        except Exception as lineplot_error:
            print(f"Error creating line plot: {lineplot_error}")

    def create_lineplot_by_date(self, year_month):
        """
        Create a line plot of daily mean temperatures for a specific date.
        Args:
            date (str): The date to plot data for in "YYYY-MM-DD" format.
        """
        try:
            # Filter data based on Year and Month.
            month_data = {key: value for key, value in self.weather_data.items() if key.startswith(year_month)}
            dates_data = []
            mean_temps = []

            if month_data:
                for date, daily_temps in month_data.items():
                    dates_data.append(date)
                    mean_temps.append(daily_temps["Mean"])

            # Create and display the line plot
                plt.plot(dates_data, mean_temps, marker='o', linestyle='-')
                plt.xlabel("Day")
                plt.ylabel("Mean Temperature (°C)")
                plt.title(f"Mean Temperatures for {year_month}")
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.show()
            else:
                print(f"Data for the date {year_month} not found.")
        except Exception as lineplot_date_error:
            print(f"Error creating line plot by date: {lineplot_date_error}")

    def days_in_month(self, year_month):
        """Get the number of days of month."""
        try:
            year, month = map(int, year_month.split('-'))
            days = calendar.monthrange(year, month)[1]
            return days
        except Exception as days_in_month_error:
            print(f"Error getting the number of days in the month: {days_in_month_error}")

if __name__ == '__main__':
    # Example usage
    # daily_temps = {"Max": 12.0, "Min": 5.6, "Mean": 7.1}
    # weather_data = {
    #     "2018-06-01": {"Max": 12.0, "Min": 5.6, "Mean": 8.1},
    #     "2018-06-02": {"Max": 22.0, "Min": 15.6, "Mean": 9.1},
    #     "2018-06-03": {"Max": 32.0, "Min": 25.6, "Mean": 5.1},
    #     "2018-06-04": {"Max": 34.0, "Min": 35.6, "Mean": 15.1}


    #     # Add more dates and daily temperature data here
    # }

    weather_data = {'1997-12-01': {'Max': -1.6, 'Min': -4.8, 'Mean': -3.2}, '1997-12-02': {'Max': -2.7, 'Min': -4.0, 'Mean': -3.4}, '1997-12-03': {'Max': -2.4, 'Min': -8.4, 'Mean': -5.4}, '1997-12-04': {'Max': -6.4, 'Min': -8.4, 'Mean': -7.4}, '1997-12-05': {'Max': -4.1, 'Min': -7.4, 'Mean': -5.8}, '1997-12-06': {'Max': -3.4, 'Min': -9.9, 'Mean': -6.7}, '1997-12-07': {'Max': -3.7, 'Min': -5.6, 'Mean': -4.7}, '1997-12-08': {'Max': -4.1, 'Min': -7.8, 'Mean': -6.0}, '1997-12-09': {'Max': -4.2, 'Min': -7.9, 'Mean': -6.1}, '1997-12-10': {'Max': -3.1, 'Min': -15.0, 'Mean': -9.1}, '1997-12-11': {'Max': -3.2, 'Min': -14.7, 'Mean': -9.0}, '1997-12-12': {'Max': 1.6, 'Min': -5.1, 'Mean': -1.8}, '1997-12-13': {'Max': 0.7, 'Min': -7.8, 'Mean': -3.6}, '1997-12-14': {'Max': 5.2, 'Min': -5.4, 'Mean': -0.1}, '1997-12-15': {'Max': 5.3, 'Min': -0.4, 'Mean': 2.5}, '1997-12-16': {'Max': 1.5, 'Min': -7.8, 'Mean': -3.2}, '1997-12-17': {'Max': 3.8, 'Min': -5.5, 'Mean': -0.9}, '1997-12-18': {'Max': 3.1, 'Min': -5.6, 'Mean': -1.3}, '1997-12-19': {'Max': -4.4, 'Min': -12.3, 'Mean': -8.4}, '1997-12-20': {'Max': -1.4, 'Min': -12.9, 'Mean': -7.2}, '1997-12-21': {'Max': -1.2, 'Min': -7.0, 'Mean': -4.1}, '1997-12-22': {'Max': -0.9, 'Min': -7.6, 'Mean': -4.3}, '1997-12-23': {'Max': 1.6, 'Min': -8.5, 'Mean': -3.5}, '1997-12-24': {'Max': 1.0, 'Min': -7.6, 'Mean': -3.3}, '1997-12-25': {'Max': -0.5, 'Min': -9.8, 'Mean': -5.2}, '1997-12-26': {'Max': -1.5, 'Min': -14.1, 'Mean': -7.8}, '1997-12-27': {'Max': -3.4, 'Min': -8.8, 'Mean': -6.1}, '1997-12-28': {'Max': -6.1, 'Min': -9.1, 'Mean': -7.6}, '1997-12-29': {'Max': -6.6, 'Min': -9.1, 'Mean': -7.9}, '1997-12-30': {'Max': -9.1, 'Min': -25.2, 'Mean': -17.2}, '1997-12-31': {'Max': 5.3, 'Min': -25.2, 'Mean': None}, '1997-11-01': {'Max': 0.3, 'Min': -1.9, 'Mean': -0.8}, '1997-11-02': {'Max': -1.8, 'Min': -5.8, 'Mean': -3.8}, '1997-11-03': {'Max': -5.2, 'Min': -6.3, 'Mean': -5.8}, '1997-11-04': {'Max': -2.8, 'Min': -5.9, 'Mean': -4.4}, '1997-11-05': {'Max': -2.3, 'Min': -4.3, 'Mean': -3.3}, '1997-11-06': {'Max': -0.2, 'Min': -4.4, 'Mean': -2.3}, '1997-11-07': {'Max': 0.4, 'Min': -2.5, 'Mean': -1.1}, '1997-11-08': {'Max': 1.0, 'Min': -2.2, 'Mean': -0.6}, '1997-11-09': {'Max': -1.3, 'Min': -12.6, 'Mean': -7.0}, '1997-11-10': {'Max': -6.3, 'Min': -12.2, 'Mean': -9.3}, '1997-11-11': {'Max': -8.6, 'Min': -16.6, 'Mean': -12.6}, '1997-11-12': {'Max': -1.9, 'Min': -10.6, 'Mean': -6.3}, '1997-11-13': {'Max': -4.2, 'Min': -11.2, 'Mean': -7.7}, '1997-11-14': {'Max': -5.0, 'Min': -14.6, 'Mean': -9.8}, '1997-11-15': {'Max': -5.0, 'Min': -9.1, 'Mean': -7.1}, '1997-11-16': {'Max': -1.6, 'Min': -9.6, 'Mean': -5.6}, '1997-11-17': {'Max': -4.3, 'Min': -7.2, 'Mean': -5.8}, '1997-11-18': {'Max': -5.9, 'Min': -12.6, 'Mean': -9.3}, '1997-11-19': {'Max': -4.3, 'Min': -15.3, 'Mean': -9.8}, '1997-11-20': {'Max': -6.7, 'Min': -13.4, 'Mean': -10.1}, '1997-11-21': {'Max': -7.3, 'Min': -19.0, 'Mean': -13.2}, '1997-11-22': {'Max': -8.0, 'Min': -12.2, 'Mean': -10.1}, '1997-11-23': {'Max': -10.8, 'Min': -21.9, 'Mean': -16.4}, '1997-11-24': {'Max': 3.2, 'Min': -14.9, 'Mean': -5.9}, '1997-11-25': {'Max': 4.0, 'Min': -1.5, 'Mean': 1.3}, '1997-11-26': {'Max': 2.7, 'Min': -4.1, 'Mean': -0.7}, '1997-11-27': {'Max': 0.1, 'Min': -8.7, 'Mean': -4.3}, '1997-11-28': {'Max': 0.0, 'Min': -7.8, 'Mean': -3.9}, '1997-11-29': {'Max': 5.4, 'Min': -4.9, 'Mean': 0.3}, '1997-11-30': {'Max': 5.4, 'Min': -21.9, 'Mean': None}, '1997-10-01': {'Max': 26.3, 'Min': 5.0, 'Mean': 15.7}, '1997-10-02': {'Max': 24.5, 'Min': 4.3, 'Mean': 14.4}, '1997-10-03': {'Max': 19.6, 'Min': 9.6, 'Mean': 14.6}, '1997-10-04': {'Max': 18.8, 'Min': 5.7, 'Mean': 12.3}, '1997-10-05': {'Max': 17.7, 'Min': 5.5, 'Mean': 11.6}, '1997-10-06': {'Max': 12.8, 'Min': 0.4, 'Mean': 6.6}, '1997-10-07': {'Max': 19.0, 'Min': -0.7, 'Mean': 9.2}, '1997-10-08': {'Max': 22.9, 'Min': 6.1, 'Mean': 14.5}, '1997-10-09': {'Max': 6.1, 'Min': 0.0, 'Mean': 3.1}, '1997-10-10': {'Max': 12.7, 'Min': -2.7, 'Mean': 5.0}, '1997-10-11': {'Max': 20.5, 'Min': 11.0, 'Mean': 15.8}, '1997-10-12': {'Max': 17.3, 'Min': 0.9, 'Mean': 9.1}, '1997-10-13': {'Max': 3.5, 'Min': -0.2, 'Mean': 1.7}, '1997-10-14': {'Max': 8.0, 'Min': 0.4, 'Mean': 4.2}, '1997-10-15': {'Max': 8.4, 'Min': -2.7, 'Mean': 2.9}, '1997-10-16': {'Max': 12.2, 'Min': 0.6, 'Mean': 6.4}, '1997-10-17': {'Max': 15.3, 'Min': 5.2, 'Mean': 10.3}, '1997-10-18': {'Max': 8.7, 'Min': 2.4, 'Mean': 5.6}, '1997-10-19': {'Max': 3.6, 'Min': -2.7, 'Mean': 0.5}, '1997-10-20': {'Max': 2.6, 'Min': -3.8, 'Mean': -0.6}, '1997-10-21': {'Max': -2.2, 'Min': -4.4, 'Mean': -3.3}, '1997-10-22': {'Max': 0.0, 'Min': -5.1, 'Mean': -2.6}, '1997-10-23': {'Max': 1.4, 'Min': -4.5, 'Mean': -1.6}, '1997-10-24': {'Max': -1.9, 'Min': -7.6, 'Mean': -4.8}, '1997-10-25': {'Max': -0.7, 'Min': -10.3, 'Mean': -5.5}, '1997-10-26': {'Max': -2.4, 'Min': -12.0, 'Mean': -7.2}, '1997-10-27': {'Max': 5.8, 'Min': -5.8, 'Mean': 0.0}, '1997-10-28': {'Max': 7.5, 'Min': -2.1, 'Mean': 2.7}, '1997-10-29': {'Max': 4.6, 'Min': -6.4, 'Mean': -0.9}, '1997-10-30': {'Max': 4.6, 'Min': 0.2, 'Mean': 2.4}, '1997-10-31': {'Max': 26.3, 'Min': -12.0, 'Mean': None}, '1997-09-01': {'Max': 19.2, 'Min': 5.5, 'Mean': 12.4}, '1997-09-02': {'Max': 18.8, 'Min': 1.1, 'Mean': 10.0}, '1997-09-03': {'Max': 21.5, 'Min': 4.5, 'Mean': 13.0}, '1997-09-04': {'Max': 25.4, 'Min': 11.0, 'Mean': 18.2}, '1997-09-05': {'Max': 21.7, 'Min': 14.9, 'Mean': 18.3}, '1997-09-06': {'Max': 18.6, 'Min': 12.0, 'Mean': 15.3}, '1997-09-07': {'Max': 26.3, 'Min': 12.1, 'Mean': 19.2}, '1997-09-08': {'Max': 21.2, 'Min': 6.4, 'Mean': 13.8}, '1997-09-09': {'Max': 19.6, 'Min': 4.6, 'Mean': 12.1}, '1997-09-10': {'Max': 24.7, 'Min': 5.7, 'Mean': 15.2}, '1997-09-11': {'Max': 28.0, 'Min': 7.6, 'Mean': 17.8}, '1997-09-12': {'Max': 21.6, 'Min': 15.5, 'Mean': 18.6}, '1997-09-13': {'Max': 28.0, 'Min': 12.4, 'Mean': 20.2}, '1997-09-14': {'Max': 17.3, 'Min': 5.9, 'Mean': 11.6}, '1997-09-15': {'Max': 18.4, 'Min': 1.4, 'Mean': 9.9}, '1997-09-16': {'Max': 22.0, 'Min': 10.4, 'Mean': 16.2}, '1997-09-17': {'Max': 19.3, 'Min': 5.6, 'Mean': 12.5}, '1997-09-18': {'Max': 14.0, 'Min': 4.3, 'Mean': 9.2}, '1997-09-19': {'Max': 11.3, 'Min': 1.0, 'Mean': 6.2}, '1997-09-20': {'Max': 14.3, 'Min': -1.0, 'Mean': 6.7}, '1997-09-21': {'Max': 25.7, 'Min': 5.9, 'Mean': 15.8}, '1997-09-22': {'Max': 16.6, 'Min': 1.5, 'Mean': 9.1}, '1997-09-23': {'Max': 21.7, 'Min': -2.4, 'Mean': 9.7}, '1997-09-24': {'Max': 30.0, 'Min': 10.0, 'Mean': 20.0}, '1997-09-25': {'Max': 25.0, 'Min': 4.2, 'Mean': 14.6}, '1997-09-26': {'Max': 27.7, 'Min': 10.7, 'Mean': 19.2}, '1997-09-27': {'Max': 24.6, 'Min': 12.3, 'Mean': 18.5}, '1997-09-28': {'Max': 15.6, 'Min': 10.9, 'Mean': 13.3}, '1997-09-29': {'Max': 12.3, 'Min': 3.0, 'Mean': 7.7}, '1997-09-30': {'Max': 30.0, 'Min': -2.4, 'Mean': None}, '1997-08-01': {'Max': 29.1, 'Min': 13.2, 'Mean': 21.2}, '1997-08-02': {'Max': 25.5, 'Min': 11.2, 'Mean': 18.4}, '1997-08-03': {'Max': 27.3, 'Min': 11.9, 'Mean': 19.6}, '1997-08-04': {'Max': 25.7, 'Min': 9.3, 'Mean': 17.5}, '1997-08-05': {'Max': 26.4, 'Min': 12.7, 'Mean': 19.6}, '1997-08-06': {'Max': 30.2, 'Min': 12.2, 'Mean': 21.2}, '1997-08-07': {'Max': 32.8, 'Min': 16.6, 'Mean': 24.7}, '1997-08-08': {'Max': 29.6, 'Min': 16.6, 'Mean': 23.1}, '1997-08-09': {'Max': 18.6, 'Min': 6.4, 'Mean': 12.5}, '1997-08-10': {'Max': 20.9, 'Min': 6.0, 'Mean': 13.5}, '1997-08-11': {'Max': 24.4, 'Min': 9.2, 'Mean': 16.8}, '1997-08-12': {'Max': 18.7, 'Min': 4.8, 'Mean': 11.8}, '1997-08-13': {'Max': 22.4, 'Min': 3.4, 'Mean': 12.9}, '1997-08-14': {'Max': 25.9, 'Min': 11.5, 'Mean': 18.7}, '1997-08-15': {'Max': 16.1, 'Min': 13.6, 'Mean': 14.9}, '1997-08-16': {'Max': 17.4, 'Min': 6.8, 'Mean': 12.1}, '1997-08-17': {'Max': 19.7, 'Min': 8.1, 'Mean': 13.9}, '1997-08-18': {'Max': 21.7, 'Min': 11.3, 'Mean': 16.5}, '1997-08-19': {'Max': 16.9, 'Min': 12.0, 'Mean': 14.5}, '1997-08-20': {'Max': 22.0, 'Min': 8.7, 'Mean': 15.4}, '1997-08-21': {'Max': 22.4, 'Min': 6.7, 'Mean': 14.6}, '1997-08-22': {'Max': 23.7, 'Min': 7.0, 'Mean': 15.4}, '1997-08-23': {'Max': 27.2, 'Min': 14.5, 'Mean': 20.9}, '1997-08-24': {'Max': 28.5, 'Min': 10.0, 'Mean': 19.3}, '1997-08-25': {'Max': 27.8, 'Min': 15.6, 'Mean': 21.7}, '1997-08-26': {'Max': 26.5, 'Min': 10.4, 'Mean': 18.5}, '1997-08-27': {'Max': 23.4, 'Min': 9.9, 'Mean': 16.7}, '1997-08-28': {'Max': 21.1, 'Min': 13.5, 'Mean': 17.3}, '1997-08-29': {'Max': 23.1, 'Min': 14.9, 'Mean': 19.0}, '1997-08-30': {'Max': 26.3, 'Min': 13.7, 'Mean': 20.0}, '1997-08-31': {'Max': 32.8, 'Min': 3.4, 'Mean': None}, '1997-07-01': {'Max': 20.0, 'Min': 10.5, 'Mean': 15.3}, '1997-07-02': {'Max': 14.1, 'Min': 10.2, 'Mean': 12.2}, '1997-07-03': {'Max': 20.2, 'Min': 10.3, 'Mean': 15.3}, '1997-07-04': {'Max': 24.8, 'Min': 11.9, 'Mean': 18.4}, '1997-07-05': {'Max': 16.8, 'Min': 6.1, 'Mean': 11.5}, '1997-07-06': {'Max': 19.3, 'Min': 2.4, 'Mean': 10.9}, '1997-07-07': {'Max': 16.3, 'Min': 10.4, 'Mean': 13.4}, '1997-07-08': {'Max': 21.0, 'Min': 13.4, 'Mean': 17.2}, '1997-07-09': {'Max': 24.5, 'Min': 14.0, 'Mean': 19.3}, '1997-07-10': {'Max': 29.4, 'Min': 16.2, 'Mean': 22.8}, '1997-07-11': {'Max': 28.8, 'Min': 19.7, 'Mean': 24.3}, '1997-07-12': {'Max': 27.1, 'Min': 19.4, 'Mean': 23.3}, '1997-07-13': {'Max': 27.1, 'Min': 18.0, 'Mean': 22.6}, '1997-07-14': {'Max': 26.4, 'Min': 16.8, 'Mean': 21.6}, '1997-07-15': {'Max': 29.0, 'Min': 15.7, 'Mean': 22.4}, '1997-07-16': {'Max': 29.4, 'Min': 14.2, 'Mean': 21.8}, '1997-07-17': {'Max': 28.4, 'Min': 14.7, 'Mean': 21.6}, '1997-07-18': {'Max': 24.0, 'Min': 15.3, 'Mean': 19.7}, '1997-07-19': {'Max': 25.7, 'Min': 13.8, 'Mean': 19.8}, '1997-07-20': {'Max': 24.9, 'Min': 13.0, 'Mean': 19.0}, '1997-07-21': {'Max': 24.7, 'Min': 13.1, 'Mean': 18.9}, '1997-07-22': {'Max': 26.6, 'Min': 15.1, 'Mean': 20.9}, '1997-07-23': {'Max': 25.3, 'Min': 17.1, 'Mean': 21.2}, '1997-07-24': {'Max': 29.4, 'Min': 17.2, 'Mean': 23.3}, '1997-07-25': {'Max': 30.3, 'Min': 17.4, 'Mean': 23.9}, '1997-07-26': {'Max': 24.5, 'Min': 14.9, 'Mean': 19.7}, '1997-07-27': {'Max': 23.1, 'Min': 11.9, 'Mean': 17.5}, '1997-07-28': {'Max': 23.5, 'Min': 8.6, 'Mean': 16.1}, '1997-07-29': {'Max': 24.9, 'Min': 6.9, 'Mean': 15.9}, '1997-07-30': {'Max': 27.8, 'Min': 10.1, 'Mean': 19.0}, '1997-07-31': {'Max': 30.3, 'Min': 2.4, 'Mean': None}, '1997-06-01': {'Max': 30.5, 'Min': 16.8, 'Mean': 23.7}, '1997-06-02': {'Max': 22.5, 'Min': 16.5, 'Mean': 19.5}, '1997-06-03': {'Max': 26.6, 'Min': 14.4, 'Mean': 20.5}, '1997-06-04': {'Max': 25.0, 'Min': 10.5, 'Mean': 17.8}, '1997-06-05': {'Max': 20.8, 'Min': 8.0, 'Mean': 14.4}, '1997-06-06': {'Max': 24.9, 'Min': 7.0, 'Mean': 16.0}, '1997-06-07': {'Max': 25.6, 'Min': 10.4, 'Mean': 18.0}, '1997-06-08': {'Max': 27.4, 'Min': 13.6, 'Mean': 20.5}, '1997-06-09': {'Max': 30.6, 'Min': 16.0, 'Mean': 23.3}, '1997-06-10': {'Max': 30.6, 'Min': 14.1, 'Mean': 22.4}, '1997-06-11': {'Max': 29.5, 'Min': 13.9, 'Mean': 21.7}, '1997-06-12': {'Max': 27.4, 'Min': 10.5, 'Mean': 19.0}, '1997-06-13': {'Max': 21.3, 'Min': 6.7, 'Mean': 14.0}, '1997-06-14': {'Max': 28.9, 'Min': 4.9, 'Mean': 16.9}, '1997-06-15': {'Max': 20.2, 'Min': 9.6, 'Mean': 14.9}, '1997-06-16': {'Max': 21.4, 'Min': 5.9, 'Mean': 13.7}, '1997-06-17': {'Max': 19.0, 'Min': 7.5, 'Mean': 13.3}, '1997-06-18': {'Max': 22.0, 'Min': 3.0, 'Mean': 12.5}, '1997-06-19': {'Max': 22.2, 'Min': 13.6, 'Mean': 17.9}, '1997-06-20': {'Max': 25.3, 'Min': 10.3, 'Mean': 17.8}, '1997-06-21': {'Max': 25.9, 'Min': 9.0, 'Mean': 17.5}, '1997-06-22': {'Max': 26.9, 'Min': 10.2, 'Mean': 18.6}, '1997-06-23': {'Max': 26.7, 'Min': 16.5, 'Mean': 21.6}, '1997-06-24': {'Max': 25.0, 'Min': 15.3, 'Mean': 20.2}, '1997-06-25': {'Max': 22.7, 'Min': 12.2, 'Mean': 17.5}, '1997-06-26': {'Max': 28.5, 'Min': 13.4, 'Mean': 21.0}, '1997-06-27': {'Max': 29.6, 'Min': 12.9, 'Mean': 21.3}, '1997-06-28': {'Max': 28.8, 'Min': 9.1, 'Mean': 19.0}, '1997-06-29': {'Max': 26.2, 'Min': 11.7, 'Mean': 19.0}, '1997-06-30': {'Max': 30.6, 'Min': 3.0, 'Mean': None}, '1997-05-01': {'Max': 10.1, 'Min': -3.0, 'Mean': 3.6}, '1997-05-02': {'Max': 11.7, 'Min': -4.7, 'Mean': 3.5}, '1997-05-03': {'Max': 12.2, 'Min': -6.3, 'Mean': 3.0}, '1997-05-04': {'Max': 20.0, 'Min': 2.7, 'Mean': 11.4}, '1997-05-05': {'Max': 13.2, 'Min': -0.8, 'Mean': 6.2}, '1997-05-06': {'Max': 15.8, 'Min': -2.3, 'Mean': 6.8}, '1997-05-07': {'Max': 11.3, 'Min': 6.8, 'Mean': 9.1}, '1997-05-08': {'Max': 8.7, 'Min': -2.3, 'Mean': 3.2}, '1997-05-09': {'Max': 16.6, 'Min': -3.5, 'Mean': 6.6}, '1997-05-10': {'Max': 22.2, 'Min': 5.5, 'Mean': 13.9}, '1997-05-11': {'Max': 10.9, 'Min': 1.3, 'Mean': 6.1}, '1997-05-12': {'Max': 7.8, 'Min': -3.4, 'Mean': 2.2}, '1997-05-13': {'Max': 4.4, 'Min': -0.3, 'Mean': 2.1}, '1997-05-14': {'Max': 2.7, 'Min': -4.6, 'Mean': -1.0}, '1997-05-15': {'Max': 8.4, 'Min': -6.8, 'Mean': 0.8}, '1997-05-16': {'Max': 16.9, 'Min': 0.2, 'Mean': 8.6}, '1997-05-17': {'Max': 14.1, 'Min': -2.9, 'Mean': 5.6}, '1997-05-18': {'Max': 7.5, 'Min': 2.7, 'Mean': 5.1}, '1997-05-19': {'Max': 10.0, 'Min': -3.7, 'Mean': 3.2}, '1997-05-20': {'Max': 10.0, 'Min': -5.5, 'Mean': 2.3}, '1997-05-21': {'Max': 15.7, 'Min': -3.4, 'Mean': 6.2}, '1997-05-22': {'Max': 13.8, 'Min': 7.9, 'Mean': 10.9}, '1997-05-23': {'Max': 15.2, 'Min': 2.7, 'Mean': 9.0}, '1997-05-24': {'Max': 15.8, 'Min': 0.3, 'Mean': 8.1}, '1997-05-25': {'Max': 17.4, 'Min': 1.4, 'Mean': 9.4}, '1997-05-26': {'Max': 19.8, 'Min': -0.4, 'Mean': 9.7}, '1997-05-27': {'Max': 22.6, 'Min': 2.6, 'Mean': 12.6}, '1997-05-28': {'Max': 23.7, 'Min': 4.3, 'Mean': 14.0}, '1997-05-29': {'Max': 24.8, 'Min': 7.6, 'Mean': 16.2}, '1997-05-30': {'Max': 28.3, 'Min': 7.6, 'Mean': 18.0}, '1997-05-31': {'Max': 29.9, 'Min': -6.8, 'Mean': None}, '1997-04-01': {'Max': 7.0, 'Min': 1.8, 'Mean': 4.4}, '1997-04-02': {'Max': 2.9, 'Min': -0.5, 'Mean': 1.2}, '1997-04-03': {'Max': 5.8, 'Min': -1.0, 'Mean': 2.4}, '1997-04-04': {'Max': 2.5, 'Min': -4.9, 'Mean': -1.2}, '1997-04-05': {'Max': -4.9, 'Min': -11.1, 'Mean': -8.0}, '1997-04-06': {'Max': -11.0, 'Min': -15.0, 'Mean': -13.0}, '1997-04-07': {'Max': -11.9, 'Min': -16.6, 'Mean': -14.3}, '1997-04-08': {'Max': -10.4, 'Min': -19.5, 'Mean': -15.0}, '1997-04-09': {'Max': -8.0, 'Min': -21.7, 'Mean': -14.9}, '1997-04-10': {'Max': -1.9, 'Min': -17.2, 'Mean': -9.6}, '1997-04-11': {'Max': 2.4, 'Min': -15.9, 'Mean': -6.8}, '1997-04-12': {'Max': 1.3, 'Min': -12.6, 'Mean': -5.7}, '1997-04-13': {'Max': 3.4, 'Min': -10.6, 'Mean': -3.6}, '1997-04-14': {'Max': 2.8, 'Min': -2.4, 'Mean': 0.2}, '1997-04-15': {'Max': -0.7, 'Min': -8.3, 'Mean': -4.5}, '1997-04-16': {'Max': -0.4, 'Min': -12.3, 'Mean': -6.4}, '1997-04-17': {'Max': 3.4, 'Min': -4.8, 'Mean': -0.7}, '1997-04-18': {'Max': 8.0, 'Min': 0.6, 'Mean': 4.3}, '1997-04-19': {'Max': 10.1, 'Min': -1.5, 'Mean': 4.3}, '1997-04-20': {'Max': 8.6, 'Min': -1.7, 'Mean': 3.5}, '1997-04-21': {'Max': 9.0, 'Min': -2.4, 'Mean': 3.3}, '1997-04-22': {'Max': 10.2, 'Min': -1.7, 'Mean': 4.3}, '1997-04-23': {'Max': 12.4, 'Min': 1.4, 'Mean': 6.9}, '1997-04-24': {'Max': 13.9, 'Min': 1.0, 'Mean': 7.5}, '1997-04-25': {'Max': 10.9, 'Min': 1.4, 'Mean': 6.2}, '1997-04-26': {'Max': 10.6, 'Min': 2.2, 'Mean': 6.4}, '1997-04-27': {'Max': 11.0, 'Min': -1.8, 'Mean': 4.6}, '1997-04-28': {'Max': 12.8, 'Min': 1.3, 'Mean': 7.1}, '1997-04-29': {'Max': 2.6, 'Min': -4.1, 'Mean': -0.8}, '1997-04-30': {'Max': 13.9, 'Min': -21.7, 'Mean': None}, '1997-03-01': {'Max': -7.7, 'Min': -19.5, 'Mean': -13.6}, '1997-03-02': {'Max': -13.1, 'Min': -24.8, 'Mean': -19.0}, '1997-03-03': {'Max': -11.1, 'Min': -22.5, 'Mean': -16.8}, '1997-03-04': {'Max': -16.0, 'Min': -24.7, 'Mean': -20.4}, '1997-03-05': {'Max': -13.3, 'Min': -23.6, 'Mean': -18.5}, '1997-03-06': {'Max': -13.1, 'Min': -26.0, 'Mean': -19.6}, '1997-03-07': {'Max': -7.7, 'Min': -22.0, 'Mean': -14.9}, '1997-03-08': {'Max': -3.3, 'Min': -19.7, 'Mean': -11.5}, '1997-03-09': {'Max': -3.8, 'Min': -9.1, 'Mean': -6.5}, '1997-03-10': {'Max': -4.0, 'Min': -14.5, 'Mean': -9.3}, '1997-03-11': {'Max': -9.8, 'Min': -21.1, 'Mean': -15.5}, '1997-03-12': {'Max': -13.3, 'Min': -27.5, 'Mean': -20.4}, '1997-03-13': {'Max': -11.3, 'Min': -23.2, 'Mean': -17.3}, '1997-03-14': {'Max': -12.7, 'Min': -24.6, 'Mean': -18.7}, '1997-03-15': {'Max': -12.1, 'Min': -24.5, 'Mean': -18.3}, '1997-03-16': {'Max': -8.8, 'Min': -24.2, 'Mean': -16.5}, '1997-03-17': {'Max': -6.4, 'Min': -19.6, 'Mean': -13.0}, '1997-03-18': {'Max': -4.1, 'Min': -21.7, 'Mean': -12.9}, '1997-03-19': {'Max': -1.3, 'Min': -10.6, 'Mean': -6.0}, '1997-03-20': {'Max': 1.4, 'Min': -14.2, 'Mean': -6.4}, '1997-03-21': {'Max': 0.1, 'Min': -4.1, 'Mean': -2.0}, '1997-03-22': {'Max': -2.0, 'Min': -13.1, 'Mean': -7.6}, '1997-03-23': {'Max': -1.0, 'Min': -15.2, 'Mean': -8.1}, '1997-03-24': {'Max': 0.2, 'Min': -2.4, 'Mean': -1.1}, '1997-03-25': {'Max': 1.8, 'Min': -7.3, 'Mean': -2.8}, '1997-03-26': {'Max': 5.9, 'Min': -2.9, 'Mean': 1.5}, '1997-03-27': {'Max': 4.7, 'Min': -4.5, 'Mean': 0.1}, '1997-03-28': {'Max': 2.1, 'Min': -3.1, 'Mean': -0.5}, '1997-03-29': {'Max': 1.7, 'Min': -7.9, 'Mean': -3.1}, '1997-03-30': {'Max': -2.1, 'Min': -8.9, 'Mean': -5.5}, '1997-03-31': {'Max': 5.9, 'Min': -27.5, 'Mean': None}, '1997-02-01': {'Max': -7.7, 'Min': -11.4, 'Mean': -9.6}, '1997-02-02': {'Max': -10.0, 'Min': -14.0, 'Mean': -12.0}, '1997-02-03': {'Max': -4.5, 'Min': -13.0, 'Mean': -8.8}, '1997-02-04': {'Max': -5.2, 'Min': -6.5, 'Mean': -5.9}, '1997-02-05': {'Max': -3.9, 'Min': -8.6, 'Mean': -6.3}, '1997-02-06': {'Max': -3.9, 'Min': -22.2, 'Mean': -13.1}, '1997-02-07': {'Max': -6.8, 'Min': -26.2, 'Mean': -16.5}, '1997-02-08': {'Max': -4.2, 'Min': -13.2, 'Mean': -8.7}, '1997-02-09': {'Max': -7.0, 'Min': -17.4, 'Mean': -12.2}, '1997-02-10': {'Max': -11.9, 'Min': -23.0, 'Mean': -17.5}, '1997-02-11': {'Max': -9.2, 'Min': -27.5, 'Mean': -18.4}, '1997-02-12': {'Max': -17.4, 'Min': -31.4, 'Mean': -24.4}, '1997-02-13': {'Max': -5.3, 'Min': -17.4, 'Mean': -11.4}, '1997-02-14': {'Max': -11.4, 'Min': -23.7, 'Mean': -17.6}, '1997-02-15': {'Max': -16.5, 'Min': -30.4, 'Mean': -23.5}, '1997-02-16': {'Max': -10.9, 'Min': -31.1, 'Mean': -21.0}, '1997-02-17': {'Max': -1.3, 'Min': -11.0, 'Mean': -6.2}, '1997-02-18': {'Max': -6.1, 'Min': -18.4, 'Mean': -12.3}, '1997-02-19': {'Max': -4.6, 'Min': -22.4, 'Mean': -13.5}, '1997-02-20': {'Max': -1.5, 'Min': -15.5, 'Mean': -8.5}, '1997-02-21': {'Max': -10.8, 'Min': -19.4, 'Mean': -15.1}, '1997-02-22': {'Max': -12.4, 'Min': -25.4, 'Mean': -18.9}, '1997-02-23': {'Max': -14.4, 'Min': -27.2, 'Mean': -20.8}, '1997-02-24': {'Max': -9.7, 'Min': -31.6, 'Mean': -20.7}, '1997-02-25': {'Max': 3.1, 'Min': -11.0, 'Mean': -4.0}, '1997-02-26': {'Max': -3.2, 'Min': -19.8, 'Mean': -11.5}, '1997-02-27': {'Max': -11.5, 'Min': -25.2, 'Mean': -18.4}, '1997-02-28': {'Max': 3.1, 'Min': -31.6, 'Mean': None}}

    plotter = PlotOperations(weather_data)
    plotter.create_boxplot(1997, 2020)
    plotter.create_lineplot(year = "1997", month = "6")
