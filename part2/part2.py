import json
from datetime import datetime
import plotly.express as px
import pandas as pd 

# df = pd.read_json(forecast_5days_a.json)
#print(df)
with open("data/forecast_5days_a.json") as json_file:
        data = json.load(json_file)
print(data)

# #STEP 1 - single time series graph that contains both min + max temps for each day 
# #define the variables 

max_temp = []
min_temp = []
converted_dates = []
# min_real_feel = []
# min_real_feelshade = [] 

for item in data["DailyForecasts"]:
        converted_dates.append(convert_date(item["Date"]))
        min_temp.append(convert_f_to_c(item["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(item["Temperature"]["Maximum"]["Value"]))
        # print(f"Minimum:{min_temp},  Maximum:{max_temp}")


#list variables in a dataframe 
# pd.DataFrame(list(map(min_temp, max_temp)))
# myData = []
# MyData = pd.DataFrame("Min":min_temp, "Max":max_temp)

# #makes the graph 
# fig = px.line(
#     NAMEOFLISTOFDICT,
#     x="Date",
#     y=["Minimum", "Maximum"],
#     title="Forecast"
# )
# fig.show()

# var1 = ["Temperature"]["Minimum"]["Value"]
# var2 = ["Temperature"]["Maximum"]["Value"]


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


# #STEP 2 - single time series graph that contains "min", min "real feel", "min real feel shade" temps 

# #show data 
# [{'date': 
# 'Monday 22 June 2020', 
# 'max': 21.7, 
# 'min': 15.0, 
# 'min real feel': 11.1, 
# 'min real feel shade': 11.1}, 

# {'date': 
# 'Tuesday 23 June 2020', 
# 'max': 19.4, 
# 'min': 11.1, 
# 'min real feel': 11.7, 
# 'min real feel shade': 11.7}, 

# {'date': 
# 'Wednesday 24 June 2020', 
# 'max': 18.9, 
# 'min': 8.9, 
# 'min real feel': 8.3, 
# 'min real feel shade': 8.3}, 

# {'date': 'Thursday 25 June 2020', 
# 'max': 20.0, 
# 'min': 11.1, 
# 'min real feel': 10.0, 
# 'min real feel shade': 10.0}, 

# {'date': 'Friday 26 June 2020', 
# 'max': 18.9, 
# 'min': 11.7, 
# 'min real feel': 10.6, 
# 'min real feel shade': 10.6}]

