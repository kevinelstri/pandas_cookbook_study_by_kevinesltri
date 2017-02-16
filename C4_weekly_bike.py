# -*-coding:utf-8-*-

# ---------------------
# Chapter 4: Find out on which weekday people bike the most with groupby and aggregate
# ---------------------

import pandas as pd
import matplotlib.pyplot as plt

'''
    4.1 Adding a 'weekday' column to our dataframe
'''
bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', index_col='Date', parse_dates=['Date'],
                    dayfirst=True)
print bikes.head()

bikes['Berri 1'].plot()  # 绘制曲线
# plt.show()

berri_bikes = bikes[['Berri 1']].copy()  # 将某一列的数据复制出来，单独为一列
print berri_bikes[:5]
print berri_bikes.index
print berri_bikes.index.day
print berri_bikes.index.weekday
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
print berri_bikes[:5]

'''
    4.2 Adding up the cyclists by weekday
'''
'''
    使用DataFrames中的.groupby()方法进行分组，并计算每一组的数量和
'''
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print weekday_counts

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print weekday_counts

weekday_counts.plot(kind='bar')
# plt.show()

'''
    4.3 Putting it together
'''
'''
    所有代码汇总
'''
bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', index_col='Date', dayfirst=True,
                    parse_dates=['Date'])
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')
plt.show()

'''
    分析：
        主要是计算时间，分组处理一周时间，将每周对应的数量加到对应的天上
    方法：
        1、csv数据的读取
        2、列数据的复制
        3、将数据按照一周来进行划分
        4、按照一周进行分组处理数据，修改索引
        5、直方图展示
'''