import pandas

FILE = "./squirrel_data.csv"

data = pandas.read_csv(FILE)
data_colors = data["Primary Fur Color"]
colors = data_colors.dropna().unique()
result_dict = {
    "color": [],
    "count": [],
}
for color in colors:
    squirrels_for_color = data[data["Primary Fur Color"] == color]
    # result[color] = squirrels_for_color.count() # Not as it seems
    result_dict["color"].append(color)
    result_dict["count"].append(len(squirrels_for_color))

print(result_dict)
df = pandas.DataFrame(result_dict)
print(df)
# df.to_csv("squirrel_count.csv")
