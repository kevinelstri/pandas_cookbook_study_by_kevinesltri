# -*-coding:utf-8-*-

# ---------------------
# Chapter 2 - Selecting data & finding the most common complaint type.ipynb
# ---------------------

import pandas as pd
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default')
# pd.set_option('display.width', 5000)
# pd.set_option('display.max_columns)', 60)
# plt.rcParams['figure.figsize'] = (15, 5)

complaints = pd.read_csv('../data/311-service-requests.csv')
print complaints.head()
print complaints['Complaint Type']
print complaints[:3]
print complaints['Complaint Type'][:3]
print complaints[:3]['Complaint Type']
print complaints[['Complaint Type', 'Borough']]
print complaints[['Complaint Type', 'Borough']][:10]
complaints_counts = complaints['Complaint Type'].value_counts()  # 计算各个元素的数量
print complaints_counts[:10]
complaints_counts[:10].plot(kind='bar')
plt.show()