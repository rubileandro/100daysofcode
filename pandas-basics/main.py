import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_fahrenheit = monday_temp * 9/5 + 32
#
# print(monday_temp_fahrenheit)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James","Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
