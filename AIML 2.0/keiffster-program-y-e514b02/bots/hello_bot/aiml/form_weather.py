from weather import Weather
import sys

base_path = sys.path[0]

cities = {'москве': 'moscow',
		  'благовещенске': 'blagoveschensk'}

w = Weather(appid='9c321878cd88f7d6721253a59639816f')

weather_aiml = ''

for city in cities.keys():
	weather_info = w.get_weather(cities[city])

	weather_aiml += '<category>\n\t <pattern> ПОГОДА В ' + city.upper() +  '</pattern>\n\t' + \
					'<template>\n\t\t' + weather_info + '\n\t</template>\n' + \
					'</category>\n\n'
				


weather_file_name = base_path + '/' + 'weather.aiml'
weather_file = open(weather_file_name, 'w')
weather_content = '<?xml version="1.0.1" encoding="UTF-8"?>\n<aiml>'

weather_content += weather_aiml

with open(base_path + '/' + 'weather.xml', 'r') as wf:
	weather_content += wf.read()

weather_content += '</aiml>'
	
weather_file.write(weather_content)
weather_file.close()
