#get the squiral data
#export the numbers of squirals of each color to that csv file

import pandas as pd

data = pd.read_csv("./squiraldata.csv")
gray_squirals = len(data[data["Primary Fur Color"] == "Gray"])
red_squirals = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirals = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirals)
# print(red_squirals)
# print(black_squirals)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirals, red_squirals, black_squirals ]
}
print(data_dict)

dataframe = pd.DataFrame(data_dict)
dataframe.to_csv("squiral_count.csv")