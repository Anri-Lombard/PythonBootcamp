import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# average = int(sum(temp_list) / len(temp_list))
# print(f"The average temperature is: {average}")

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition)

# print(data[data.day == "Monday"])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# data_dict = {
#     "students": ["Anri", "Elon", "Bill", "Mark"],
#     "scores": [76, 34, 56, 99]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
gray_amount = len(gray)
cinnamon_amount = len(cinnamon)
black_amount = len(black)

squirrel_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_amount, cinnamon_amount, black_amount]
}

pandas.DataFrame(squirrel_dict).to_csv("squirrel_census.csv")
