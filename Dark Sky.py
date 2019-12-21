# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:36:22 2019

@author: hirsh
"""


from forecastiopy import *
import pandas as pd
import numpy as np

api_key = '27744a89be3f482df1151b3cc340cbc0'

loc = [\
  [ "Anchorage, Alaska", 61.2181, -149.9003 ],\
  [ "Buenos Aires, Argentia", -34.6037, -58.3816 ],\
  [ "Sao Jose dos Campos, Brazil", -23.2237, -45.9009 ],\
  ["San José, Costa Rica", 9.9281, -84.0907],\
  ["Nanaimo, Canada", 49.1659, -123.9401],\
  ["Ningbo, China", 29.8683, 121.5440],\
  ["Giza, Egypt", 30.0131, 31.2089],\
  ["Mannheim, Germany", 49.4875, 8.4660],\
  ["Hyderabad, India", 17.3850, 78.4867],\
  ["Tehran, Iran", 35.6892, 51.3890],\
  ["Bishkek, Kyrgyzstan", 42.8746, 74.5698],\
  ["Riga, Latvia", 56.9496, 24.1052],\
  ["Quetta, Pakistan", 30.1798, 66.9750],\
  ["Warsaw, Poland", 52.2297, 21.0122],\
  ["Dhahran, Saudia Arabia", 26.2361, 50.0393],\
  [ "Madrid, Spain", 40.4168, -3.7038 ],\
  [ "Oldham, United Kingdom", 53.5409, -2.1114 ]\
]

col = ['City','Min 1','Min 2','Min 3','Min 4','Min 5','Max 1','Max 2','Max 3','Max 4','Max 5','Min Avg','Max Avg']
data = []
for i in range(len(loc)):
    City = []
    Min = []
    Max = []
    AvgMin = []
    AvgMax = []
    city = loc[i][0]
    City.append(city)
    weather = ForecastIO.ForecastIO(api_key, latitude=loc[i][1], longitude=loc[i][2], units='uk')
    daily = FIODaily.FIODaily(weather)
    for day in range(2,7):
        val = daily.get(day)
        MinTemp = val['temperatureMin']
        Min.append(MinTemp)
        MaxTemp = val['temperatureMax']
        Max.append(MaxTemp)
    avg_min = round(np.sum(Min) / 5,2)
    AvgMin.append(avg_min)
    avg_max = round(np.sum(Max) / 5,2)
    AvgMax.append(avg_max)
    concat = np.concatenate((City,Min,Max, AvgMin, AvgMax), axis=0)
    data.append(concat)
df = pd.DataFrame(data, columns=col)
df = df[['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2', 'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min 5', 'Max 5', 'Min Avg', 'Max Avg']] # re-order columns
df.to_csv('temp.csv')