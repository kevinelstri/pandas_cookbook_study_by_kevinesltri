# -*-coding:utf-8-*-

#  by kevinelstri
#  2017.2.17

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------
# Chapter 5: Combining dataframes and scraping Canadian weather data
# ---------------------

'''
    Summary
'''
weather_2012_final = pd.read_csv('../data/weather_2012.csv', index_col='Date/Time')
print weather_2012_final.head()
weather_2012_final['Temp (C)'].plot(figsize=(15, 6))
# plt.show()

'''
    5.1 Downloading one month of weather data
'''
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)
print weather_mar2012

weather_mar2012['Temp (C)'].plot(figsize=(15, 5))  # 图形展示温度变化情况
plt.show()

weather_mar2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)',
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag',
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag',
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill',
    u'Wind Chill Flag', u'Weather']

weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')  # drop the column if any value is null 删除空列
print weather_mar2012[:5]

weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
print weather_mar2012[:5]

'''
    5.2 Plotting the temperature by hour of day
'''
temperatures = weather_mar2012[['Temp (C)']].copy()
print temperatures.head()

temperatures.loc[:, 'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()
plt.show()

'''
    5.3 Getting the whole year of data
'''


def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


print download_weather_month(2012, 1)[:5]

data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]  # 所有月份

weather_2012 = pd.concat(data_by_month)
print weather_2012

'''
    5.4 Saving to a CSV
'''
weather_2012.to_csv('../data/weather_2012.csv')
