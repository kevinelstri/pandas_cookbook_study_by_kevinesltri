# -*-coding:utf-8-*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------
# Chapter 7 - Cleaning up messy data.ipynb  清理垃圾数据
# ---------------------

requests = pd.read_csv('../data/311-service-requests.csv')
# print requests.head()

'''
    7.1 How do we know if it's messy?
'''
zip = requests['Incident Zip'].unique()  # unique()用于查看所有的值
# print zip
'''
    zip中存在的问题：
        1、数据类型问题，有些是字符串型，有些是浮点型
        2、有一些值不存在nan
        3、有些值不正确 83  29616-0759
        4、有N/A值，pandas不能够识别，'N/A','NO CLUE'
    处理方法：
        1、使'N/A','NO CLUE'变成规则的nan
        2、使所有格式都变成字符串
'''

'''
    7.3 Fixing the nan values and string/float confusion
'''
na_value = ['N/A', 'NO CLUE', 'O', 'nan']
requests = pd.read_csv('../data/311-service-requests.csv', na_values=na_value, dtype={'Incident Zip': str})
# 读取csv文件时，将异常值设置为空值，将数据类型全部转换为字符串类型
zip = requests['Incident Zip'].copy()
# print zip.unique()

'''
    7.4 What's up with the dashes? 处理数字之间的横杠29616-0759
'''
row_with_dashs = requests['Incident Zip'].str.contains('-').fillna(False)  # 将带横杠的全部提取出来
# print len(requests[row_with_dashs])
# print requests[row_with_dashs]

requests['Incident Zip'][row_with_dashs] = np.nan  # 将带横杠的全部转换为空值
# print requests['Incident Zip'].unique()

long_zip_codes = requests['Incident Zip'].str.len() > 5
# print requests['Incident Zip'][long_zip_codes].unique()

requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)  # slice()获取字符串的指定长度
# requests['Incident Zip'] = requests['Incident Zip'].str[0:5]
# print requests['Incident Zip'].unique()

# requests[requests['Incident Zip']] == '00000'

zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

unique_zips = requests['Incident Zip'].unique()
unique_zips.sort()  # 排序
print unique_zips

zips = requests['Incident Zip']
is_close = zips.str.startswith('0') | zips.str.startswith('1')  # zip以0或1开头
is_far = ~(is_close) & zips.notnull()

print zips[is_far]

print requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort('Incident Zip')

print requests['City'].str.upper().value_counts()  # 城市名转换为大写的，并且统计城市的数量

'''
    7.5 Putting it together
'''
# 异常值处理及csv文件的读取
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('../data/311-service-requests.csv',
                       na_values=na_values,
                       dtype={'Incident Zip': str})


# 将邮政编码的位数固定为5位
def fix_zip_codes(zips):
    zips = zips.str.slice(0, 5)

    zero_zips = zips == '00000'
    zips[zero_zips] = np.nan

    return zips


requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])
print requests['Incident Zip'].unique()
