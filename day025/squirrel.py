import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = squirrel_data["Primary Fur Color"].dropna()
squirrel_counts = {}
squirrel_counts["Color"] = colors.unique()
squirrel_counts["Count"] = []

for color in colors.unique():
    squirrel_counts["Count"].append(len(squirrel_data[squirrel_data["Primary Fur Color"] == color]))
data = pandas.DataFrame(squirrel_counts)
print(data)