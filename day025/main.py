from numpy import average
import pandas

data = pandas.read_csv("./weather_data.csv")
#this should be a DataFrame
# print(type(data))
#columns are Series
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)
# print(data)
# print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)
print(average(temp_list))
print(data["temp"].mean())
print(data["temp"].max())
print(data.temp.max())

#get data from a row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(int(monday.temp) * 9 / 5 + 32)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Steve"],
    "scores": [56, 76, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)