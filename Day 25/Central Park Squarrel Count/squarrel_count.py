import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df = pd.DataFrame(data)

cinnamon_squarrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squarrel_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squarrel_count = len(data[data["Primary Fur Color"] == "Gray"])


color_dict = {
    "Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon_squarrel_count, gray_squarrel_count, black_squarrel_count]
}

data = pd.DataFrame(color_dict)
data.to_csv("squarrel_count.csv")
