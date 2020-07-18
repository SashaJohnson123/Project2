import json
from datetime import datetime
​
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"
​
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"
​
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')
​
​
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius
​
    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    pass
​
def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass
​
​
​
forecast_file = "data/forecast_5days_a.json"
​
with open(forecast_file) as json_file:
   data = json.load(json_file)

