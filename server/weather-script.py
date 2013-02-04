#!/usr/bin/python2

# Kindle Weather Display
# Matthew Petroff (http://www.mpetroff.net/)
# September 2012
# Reventlov Giskard (http://volcanis.me/)

import datetime
import codecs
import urllib2
import json

highs = [None]*4
lows = [None]*4
icons = [None]*4

weather_json = urllib2.urlopen('http://api.wunderground.com/api/PUT-API-KEY-HERE/forecast/q/PUT-CITY-HERE.json')
json_string = weather_json.read()
parsed_json = json.loads(json_string)

highs[0] = parsed_json['forecast']['simpleforecast']['forecastday'][0]['high']['celsius']
lows[0] = parsed_json['forecast']['simpleforecast']['forecastday'][0]['low']['celsius']
icons[0] = parsed_json['forecast']['simpleforecast']['forecastday'][0]['icon']

highs[1] = parsed_json['forecast']['simpleforecast']['forecastday'][1]['high']['celsius']
lows[1] = parsed_json['forecast']['simpleforecast']['forecastday'][1]['low']['celsius']
icons[1] = parsed_json['forecast']['simpleforecast']['forecastday'][1]['icon']

highs[2] = parsed_json['forecast']['simpleforecast']['forecastday'][2]['high']['celsius']
lows[2] = parsed_json['forecast']['simpleforecast']['forecastday'][2]['low']['celsius']
icons[2] = parsed_json['forecast']['simpleforecast']['forecastday'][2]['icon']

highs[3] = parsed_json['forecast']['simpleforecast']['forecastday'][3]['high']['celsius']
lows[3] = parsed_json['forecast']['simpleforecast']['forecastday'][3]['low']['celsius']
icons[3] = parsed_json['forecast']['simpleforecast']['forecastday'][3]['icon']

weather_json.close()

# Parse dates
day_one = datetime.datetime.now()

#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r', encoding='utf-8').read()

# Insert icons and temperatures
output = output.replace('ICON_ONE',icons[0]).replace('ICON_TWO',icons[1]).replace('ICON_THREE',icons[2]).replace('ICON_FOUR',icons[3])
output = output.replace('HIGH_ONE',str(highs[0])).replace('HIGH_TWO',str(highs[1])).replace('HIGH_THREE',str(highs[2])).replace('HIGH_FOUR',str(highs[3]))
output = output.replace('LOW_ONE',str(lows[0])).replace('LOW_TWO',str(lows[1])).replace('LOW_THREE',str(lows[2])).replace('LOW_FOUR',str(lows[3]))

# Insert days of week
one_day = datetime.timedelta(days=1)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
output = output.replace('DAY_THREE',days_of_week[(day_one + 2*one_day).weekday()]).replace('DAY_FOUR',days_of_week[(day_one + 3*one_day).weekday()])

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)
