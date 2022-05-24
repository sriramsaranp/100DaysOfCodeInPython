# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         else :
#             temperature.append(int(row[1]))

#     print(temperature)


import pandas

# data = pandas.read_csv("weather_data.csv")

# # print(type(data))
# data_temp = data["temp"].to_list()
# # print(type(data_temp[0]))


# avg = data["temp"].max()

# print(avg)

#Get data in columns
# print(data.condition)
# print(data["condition"])

#Get data in Rows
# print(data[data.day == "Monday"])

#Challenge. Print the row of the data with maximum temperature

# print(data[data.temp == data.temp.max()])

#Challenge to print the temp of a given day in farenheit

# monday = data[data.day == "Monday"]

# monday_temp_farenheit = 32 + 9*(monday.temp)/5
# print(monday_temp_farenheit)


#Creating a new data frame from scratch
# data_dict = {
#     "name" : ["amy","jake","boyle"],
#     "scores": [75,80,78]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_color = data["Primary Fur Color"].to_list()
# print(squirrel_color)
gray_squirrel = squirrel_color.count("Gray")
cinnamon_squirrel = squirrel_color.count("Cinnamon")
black_squirrel = squirrel_color.count("Black")

# print(gray_squirrel)
# print(cinnamon_squirrel)
# print(black_squirrel)
new_data = {
    "fur color" : ["gray","cinnamon","black"],
    "count" : [gray_squirrel,cinnamon_squirrel,black_squirrel]
} 


squirrel_color_count = pandas.DataFrame.from_dict(new_data)

squirrel_color_count.to_csv("squirrel_color_final.csv")
