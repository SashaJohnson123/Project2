import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celcius = (temp_in_farenheit - 32)*5/9
    temp_in_celcius = round(temp_in_celcius, 1)
    return temp_in_celcius


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total/num_items
    #use the round() function to get it right
    #round it to one decimal case
    mean = round(mean, 1)
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.
    
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    
    with open(forecast_file) as json_file:
        data = json.load(json_file)

    #STEP 1: Initialise all the variables that you will need in your loop
    min_temp = []
    max_temp = []
    date = []
    precipitation_probability = []
    long_words = []
    rain_chance = [] 
    long_boy = []
    long_boy_night = []
    rain_chance_night  = []
    converted_dates = []
    highest_temp = []
    lowest_temp = []
    line = [] 
    max_mean = []
    min_mean = [] 
    date_input = []
    low_day = []
    high_day = []
    num_items = 0 

    num_items = num_items + 1 

    #you need 7 in total + optional extras 

    #STEP 2: Do a "for" loop to get the values from the dataset
    for item in data["DailyForecasts"]:
        converted_dates.append(convert_date(item["Date"]))
        min_temp.append(convert_f_to_c(item["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(item["Temperature"]["Maximum"]["Value"]))
        # print(f"Minimum:{min_temp},  Maximum:{max_temp}")
        long_boy.append(item["Day"]["LongPhrase"])
        rain_chance.append(item["Day"]["RainProbability"])
        long_boy_night.append(item["Night"]["LongPhrase"])
        rain_chance_night.append(item["Night"]["RainProbability"])
        # print(f"Long words: {long_boy}")
        # print(f"Chance of rain{rain_chance} Long_words:  {long_boy}") 
        # converted_dates.append(convert_date(date_input))
        # max_temp = format_temperature(max_temp)
        # min_temp = format_temperature(min_temp)


    #STEP 3: Calculate the things necessary for the "overview" (mean, overall min etc.)
    # min_temp = [8.3, 10.6, 14.4, 14.4, 10.6]
    # max_temp = [17.8, 19.4, 22.2, 22.2, 18.9]
    #input data 
    # date_input = weather["Date"]
    # date = convert_date(date_input)
    # #calculate min and max 
    # min_temp = convert_f_to_c(min_temp)
    # max_temp = convert_f_to_c(max_temp)
    #add values to perform calc 
    # min_mean = sum(min_temp)/(len(min_temp))
    # max_mean = sum(max_temp)/(len(max_temp))
    #return calc 
    min_mean = calculate_mean(sum(min_temp), len(min_temp))
    max_mean = calculate_mean(sum(max_temp), len(max_temp))
    #determine day/ lowest temp 
    index_min = min_temp.index(min(min_temp))
    low_day = converted_dates[index_min]
    index_max = max_temp.index(max(max_temp))
    high_day = converted_dates[index_max]

    # example: date = [date1, date2, date3, date4, date5]
    #google "python find the minimum in a list"
    #google "python find index of a value in a list"
    #date_min = date[index_of_min] 

# STEP 4: Create the lines for the overview information one by one, append each to the output
    output = []
    line = ("{} Day Overview".format(len(min_temp)))
    output.append(line)
    line = f"    The lowest temperature will be {min(min_temp)}{DEGREE_SYBMOL}, and will occur on {low_day}."
    output.append(line)
    line = f"    The highest temperature will be {max(max_temp)}{DEGREE_SYBMOL}, and will occur on {high_day}."
    output.append(line)
    line = f"    The average low this week is {min_mean}{DEGREE_SYBMOL}."
    output.append(line)
    line = f"    The average high this week is {max_mean}{DEGREE_SYBMOL}."
    output.append(line)
    output.append("")
    # line = "another line {}".format(variable)
    # output.append(line)
    # STEP 5: Loop 1 for daily output,  append each line to output
    # or While Loop 2 for each day/ value output
    for i in range(len(min_temp)):
        line = ("-------- " + converted_dates[i] + " --------")
        output.append(line)
        line = f"Minimum Temperature: {min_temp[i]}{DEGREE_SYBMOL}"
        output.append(line)
        line = f"Maximum Temperature: {max_temp[i]}{DEGREE_SYBMOL}"
        output.append(line)
        line = f"Daytime: {long_boy[i]}\n    Chance of rain:  {rain_chance[i]}%"
        output.append(line)
        line = f"Nighttime: {long_boy_night[i]}\n    Chance of rain:  {rain_chance_night[i]}%"
        output.append(line)
        output.append("")
    # # STEP 6: Join all in the one string
    output.append("")
    final_output = "\n".join(output)
    return(final_output)
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))

