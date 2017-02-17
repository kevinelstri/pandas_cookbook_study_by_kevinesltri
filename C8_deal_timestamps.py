# -*-coding:utf-8-*-

#  by kevinelstri
#  2017.2.17

# ---------------------
# Chapter 8 - How to deal with timestamps.ipynb
# ---------------------

import pandas as pd

'''
    8.1 Parsing Unix timestamps
'''
popcon = pd.read_csv('../data/popularity-contest', sep=' ')
# print popcon.head()
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
# print popcon[:5]
print popcon['atime'].dtype

popcon['atime'] = popcon['atime'].astype(int)
# print popcon['atime'][:5]
# popcon['ctime'] = popcon['ctime'].astype(int)
popcon['atime'] = pd.to_datetime(popcon['atime'])
# popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')
# print popcon['atime'][:5]

popcon = popcon[popcon['atime'] > '1970-01-01']
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
nonlibraries.sort('ctime', ascending=False)[:10]
