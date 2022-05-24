from dotenv import load_dotenv
from os import environ as env
from pprint import pprint as pp
import requests as r

from helpers import to_dict

load_dotenv()

API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(lat, lon):
	resp = r.get(API_URL, params={
		'lat': lat,
		'lon': lon,
		'appid': env.get('API_KEY', ''),
		'units': 'metric'
	})

	results = resp.json()

	location = results.get('name')
	weather = results.get('weather')[0]
	description = weather.get('description')
	icon = weather.get('icon')
	icon = f'http://openweathermap.org/img/wn/{icon}@2x.png'
	temp = results.get('main').get('temp')
	temp_felt = results.get('main').get('feels_like')
	temp_min = results.get('main').get('temp_min')
	temp_max = results.get('main').get('temp_max')
	pressure = results.get('main').get('pressure')
	humidity = results.get('main').get('humidity')
	sea_level = results.get('main').get('sea_level')
	wind_speed = results.get('wind').get('speed')
	wind_direction = results.get('wind').get('deg')
	wind_gust = results.get('wind').get('gust')

	if wind_direction <= 45 or wind_direction > 315:
		wind_direction = 'north'
	elif wind_direction <= 135 or wind_direction > 45:
		wind_direction = 'east'
	elif wind_direction <= 225 or wind_direction > 135:
		wind_direction = 'south'
	else:
		wind_direction = 'west'

	timezone = results.get('timezone')

	timezone_pos = timezone >= 0
	if not timezone_pos:
		timezone *= -1

	hours = timezone // 3600
	minutes = (timezone % 3600) // 60

	timezone = f'{"+" if timezone_pos else "-"}{hours:02d}:{minutes:02d}'

	return to_dict(
		location=location,
		description=description,
		icon=icon,

		temp=temp,
		temp_felt=temp_felt,
		temp_min=temp_min,
		temp_max=temp_max,

		timezone=timezone,

		pressure=pressure,
		humidity=humidity,
		sea_level=sea_level,

		wind_speed=wind_speed,
		wind_direction=wind_direction,
		wind_gust=wind_gust
	)

if __name__ == '__main__':
	data = get_weather_data(lat=24.434727, lon=77.162304)
	pp(data)