import requests
import time
from bs4 import BeautifulSoup as bs
from webscraping import Web_Scraping
import pandas as pd
def citydatacsv(city_name):
    city_weather_info = Web_Scraping()
    new_time, feel_temp, weather, temp_d, wind_speed, humidity, precipitation = city_weather_info.city_scraping(city=city_name)
    df = pd.DataFrame()
    df['time'] = new_time
    df['temperature'] = temp_d
    df['feels_like'] = feel_temp
    df['wind speed'] = wind_speed
    df['humidity'] = humidity
    df['precipitation'] = precipitation
    df['weather'] = weather
    time.sleep(2)
    filename = city_name + '.csv'
    df.to_csv(r'static/data/{}'.format(filename))

cities=['kolkata','agartala','bangalore','bhubaneswar','chennai',
        'delhi','hyderabad','indore','jaipur','kanpur','lucknow','mumbai','nagpur','nainital','noida','pune','surat','visakhapatnam']

for i in cities:
    citydatacsv(i)