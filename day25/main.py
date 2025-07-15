# import csv

# with open("./weather_data.csv", mode="r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather-data.csv")
# print(data["temp"])

#*calculate statistics of temperature
# print(data["temp"].mean())
# print(data["temp"].max())

#*get data in a column
# print(data["condition"])
# print(data.day)

#*get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#*crete a dataframe from scratch
# data_dict = {
#     "students": ["Amey", "Hiki", "Shiro"],
#     "score":["69", "100", "84"]
# }
# data = pd.DataFrame(data_dict)
# print(data)