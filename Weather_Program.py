# Part 1: Uses urllib.request that accesses data from 4 US cities + prompts user input

print("Your Weather Report")
print()
print("Current observations are available for: ")
cities = ["Chicago", "Miami", "Los Angeles", "New York"]
for city in cities:
    print("- "+city)

print()
user_city = input("Enter the city you would like a weather report for: ").title()
while True:
    if user_city in cities:
        print("Accessing weather data . . .")
        break
    else:
        user_city = input("No data available. Please try another city: ").title()

import urllib.request
if user_city == "Chicago":
    page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KORD.xml')
    source_code = page.read()
    source_string = str(source_code)
elif user_city == "Miami":
    page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KMIA.xml')
    source_code = page.read()
    source_string = str(source_code)
elif user_city == "Los Angeles":
    page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KLAX.xml')
    source_code = page.read()
    source_string = str(source_code)
elif user_city == "New York":
    page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KJFK.xml')
    source_code = page.read()
    source_string = str(source_code)

# Comment

# Part 2: Reads/converts data to string + parses data to find 6 pieces of info

city_weather={}
def get_parts(text):
    location_start = source_string.find(text+">")
    location_end = source_string.find("</"+text+">")
    location_string = source_string[location_start:location_end]
    location_list = location_string.split(">")
    city_weather[location_list[0]] = location_list[1]
    return city_weather

print()

get_parts("location")
get_parts("weather")
get_parts("temperature_string")
get_parts("relative_humidity")
get_parts("wind_string")
get_parts("observation_time")

location = city_weather["location"]
current_weather = city_weather["weather"]
temp = city_weather["temperature_string"]
temp = temp[0:4]
humidity = (city_weather["relative_humidity"] + "%")
wind = city_weather["wind_string"]
date_time = city_weather["observation_time"]

city_weather["Location"] = city_weather.pop("location")
city_weather["Weather"] = city_weather.pop("weather")
city_weather["Temperature"] = city_weather.pop("temperature_string")
city_weather["Temperature"] = temp + " degrees F"
city_weather["Humidity"] = city_weather.pop("relative_humidity")
city_weather["Humidity"] = city_weather["Humidity"] + "%"
city_weather["Wind"] = city_weather.pop("wind_string")
city_weather["Observation"] = city_weather.pop("observation_time")

print("The current weather has been accessed for", user_city)
print()


# Part 3: With info in dict, prompts user for desired info + reprompts

print("Information available:")
info_list = ["location", "weather", "temperature", "humidity", "wind", "observation"]
for data in info_list:
    print("- " + data)

print()

inquiry = input("What weather information would you like? ").lower()
while inquiry != "done":
    if inquiry in info_list:
        if inquiry == "location":
            print("The location is", user_city)
            print()
        elif inquiry == "weather":
            print("The current weather in", user_city, "is", current_weather)
            print()
        elif inquiry == "temperature":
            print("The temperature in", user_city, "is", temp, "degrees F")
            print()
        elif inquiry == "humidity":
            print("The humidity in", user_city, "is", humidity)
            print()
        elif inquiry == "wind":
            print("The wind in", user_city, "is", wind)
            print()
        else:
            print("The date and time of weather observation in", user_city, "is", date_time)
            print()
    else:
        print("That data is not available.")
        print()
    inquiry = input('What weather information would you like? Or, to end, enter "done". ').lower()


# Part 4: Option to print full report to external OS file

print()
file = input("Would you like to export the full weather report? (yes/no) ").lower()

if file == "yes":
    file_object = open("weather_report.txt", 'w')
    file_object.write("Weather for " + user_city + "\n")
    file_object.write("\n")
    for item in city_weather:
        file_object.write(item + ": " + city_weather[item] + "\n")
    file_object.close()
    print("The full weather report has been exported.")
else:
    print("Goodbye")

   

 

