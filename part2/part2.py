import json
from datetime import datetime
import plotly.express as px
import pandas as pd 


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    # print("hello")
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

# df = pd.read_json(forecast_5days_a.json)
#print(df)
with open("data/forecast_5days_a.json") as json_file:
        data = json.load(json_file)
# print(data)

# #STEP 1 - single time series graph that contains both min + max temps for each day 
# #define the variables 
max_temp_1 = []
min_temp_1 = []
converted_dates = []
min_real_feel = []
min_real_feelshade = [] 

# forecast = [] 

for item in data["DailyForecasts"]:
        # converted_dates.append(convert_date(item["Date"]))
        converted_dates.append(convert_date(item["Date"]))
        # min_temp.append(convert_f_to_c(item["Temperature"]["Minimum"]["Value"]))
        # max_temp.append(convert_f_to_c(item["Temperature"]["Maximum"]["Value"]))
        # print(f"Minimum:{min_temp},  Maximum:{max_temp}")
        min_temp_1.append(convert_f_to_c(item["Temperature"]["Minimum"]["Value"]))
        max_temp_1.append(convert_f_to_c(item["Temperature"]["Maximum"]["Value"]))
        min_real_feel.append(convert_f_to_c(item["RealFeelTemperature"]["Minimum"]["Value"]))
        min_real_feelshade.append(convert_f_to_c(item["RealFeelTemperatureShade"]["Minimum"]["Value"]))

data_1 = {
    "Date": converted_dates, 
    "Minimum Temperature": min_temp_1, 
    "Maximum Temperature": max_temp_1, 
    "Minimum Real Feel": min_real_feel, 
    "Minimum Real Feel Shade": min_real_feelshade, 
}

# forecast.append(data_1)
# print(data_1)

#makes the graph 
# fig = px.line(data_1, 
#     x="Date",
#     y=["Minimum Temperature", "Maximum Temperature"], 
#     # y=[min_temp_1, max_temp_1],
#     title="Forecast")
# fig.show()

fig2 = px.line(data_1, 
    x="Date",
    y=["Minimum Temperature", "Minimum Real Feel", "Minimum Real Feel Shade"], 
    # y=[min_temp_1, max_temp_1],
    title="Forecast")
fig2.show()


# # # Line Graphs
# fig = px.line(df, x="Temperature", y="Day", title="Minimum and Maximum Temperatures per Day", template="plotly_dark")
# fig.update_layout(plot_bgcolor= "white")
# fig.update_xaxes(gridcolor='LightGrey')
# fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGrey')
# ​
# fig.update_traces(line = dict(color='royalblue', width=3, dash='dash'), 
#     mode='lines+markers',
#     marker=dict(
#             color='LightSkyBlue',
#             size=10,
#             line=dict(
#                 color='royalblue',
#                 width=2
#             )
# ))

# #list variables in a dataframe 
# # pd.DataFrame(list(map(min_temp, max_temp)))
# # myData = []
# # MyData = pd.DataFrame("Min":min_temp, "Max":max_temp)


# # Using hard coded data df = {
# # "our_data": [123, 132, 654, 345, 125, 498], "more_data": [345, 67, 176, 245, 197, 391], "columns": ["a", "b", "c", "d", "e", "f"]
# # }
# fig = px.line(df, y="our_data", x="columns") fig.show()
# fig = px.line(df, y=["our_data", "more_data"], x="columns") fig.show()

# var1 = ["Temperature"]["Minimum"]["Value"]
# var2 = ["Temperature"]["Maximum"]["Value"]


# #STEP 2 - single time series graph that contains "min", min "real feel", "min real feel shade" temps 

