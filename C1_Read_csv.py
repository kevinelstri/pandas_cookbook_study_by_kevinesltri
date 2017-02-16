# -*-coding:utf-8-*-

# ---------------------
# Chapter 1 - Reading from a CSV.ipynb
# ---------------------

import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default')  # 使图像更漂亮
# pd.set_option('matplotlib.pyplot.style.use', 'default')
# plt.rcParams['figure.figsize'] = (15, 5)

'''
    1.1 Reading data from a csv file
'''
broken_df = pd.read_csv('../data/bikes.csv')
# print broken_df[:3]

# seq为分隔符，encoding为编码，index_col为索引列编号，dayfirst为日期格式，parse_dates为日期解析
fixed_df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
print fixed_df[:3]
print type(fixed_df)  # <class 'pandas.core.frame.DataFrame'>
print

'''
    1.2 Selecting a column
'''
print fixed_df['Berri 1']

'''
    1.3 Plotting a column
'''
fixed_df['Berri 1'].plot()
plt.show()

fixed_df.plot(figsize=(15, 10))
plt.show()

'''
    1.4 Putting all that together
'''
df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
df['Berri 1'].plot()
plt.show()
