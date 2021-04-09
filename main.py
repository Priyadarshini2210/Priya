import requests
from datetime import datetime

user_api = "c1d2ef4f11414f7c642cda7dcf3da271"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


WeatherFile=open("WeatherFile.txt","a+")
WeatherFile.write(f"{location}" '\n')
WeatherFile.write(f"Temperature: {temp_city}" '\n')
WeatherFile.write(f"Humidity: {hmdt}" '\n')
WeatherFile.write(f"DateAndTime: {date_time}" '\n')
WeatherFile.write(f"Weather Report: {weather_desc}" '\n')
WeatherFile.read()
WeatherFile.close()
