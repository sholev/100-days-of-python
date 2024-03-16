import csv

FILE = "./weather_data.csv"

# with open(FILE) as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     temp_index = -1
#     for row in data:
#         if temp_index < 0:
#             temp_index = row.index("temp")
#         else:
#             temps.append(int(row[temp_index]))
#     print(temps)

import pandas

data = pandas.read_csv(FILE)
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(data["temp"].mean())

# Get data columns
print(data.temp.min())
print(data.temp.max())
print(data.condition)

# Get data row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp_C = monday.temp[0]
monday_temp_F = (1.8 * monday_temp_C) + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")