# -*-coding:utf-8-*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------
# Chapter 6 - String Operations- Which month was the snowiest.ipynb
# ---------------------

weather_2012 = pd.read_csv('../data/weather_2012.csv', encoding='latin1', index_col='Date/Time', parse_dates=True)
print weather_2012.head()

'''
    6.1 String operations
'''
weather_description = weather_2012['Weather']  # 取出天气那一列
is_snowing = weather_description.str.contains(
    'Snow')  # 天气是否为snow，若天气为snow，返回True,否则返回False；str将类型转换成字符串形式，利于字符串的匹配、替换和截取
print is_snowing[:5]
is_snowing.plot()  # 将一年中下雪的天全部显示出来
plt.show()

'''
    6.2 Use resampling to find the snowiest month 寻找下雪最多的月份
'''
'''
    每个月份的平均气温，可以使用resample()方法来实现
'''
weather_2012['Temp (C)'].resample('M', how=np.median).plot(kind='bar')  # 平均气温
plt.show()

# 将天气情况使用0和1来表示，若为snow，也就是True，则返回1，否则用0表示
print is_snowing.astype(float)[:10]  # astype用于类型转换，bool类型转换为float类型

# 使用resample()查找出每个月下雪的可能性，用百分比来表示
print is_snowing.astype(float).resample('M', how=np.mean)  # 'M':表示按月的时间频率

is_snowing.astype(float).resample('M', how=np.mean).plot(kind='bar')
plt.show()

'''
    6.3 Plotting temperature and snowiness stats together  温度和下雪一起分析
'''
temperature = weather_2012['Temp (C)'].resample('M', how=np.median)  # 平均温度
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M', how=np.mean)  # 下雪比例

temperature.name = 'Temperature'
snowiness.name = 'Snowiness'

stats = pd.concat([temperature, snowiness], axis=1)
print stats
stats.plot(kind='bar')  # 下雪比例在图示中显示太小，所以这里不合理
plt.show()

stats.plot(kind='bar', subplots=True, figsize=(15, 10))  # 将两张图放到一个平面上，分开放，这样就能合理的进行图像展示
plt.show()

# subplot()作用：将多个figure放到一个平面上
