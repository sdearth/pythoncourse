import csv

with open("./weather_data.csv") as weather_file:
    data = csv.DictReader(weather_file)
    temperatures = []
    for row in data:
        temperatures.append(int(row['temp']))
    
print(temperatures)