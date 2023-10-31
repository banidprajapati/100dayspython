# without using any library

# with open("weather_data.csv") as data:
#     container = data.readlines()
# print(container)


# using csv library

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#         # print(row)
#             temperature.append(int(row[1]))
# print(temperature)

# using pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
print(data[data.day == "Monday"].count())
# print(average)
