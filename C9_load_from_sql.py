# -*-coding:utf-8-*-

#  by kevinelstri
#  2017.2.17

# ---------------------
# Chapter 9 - Loading data from SQL databases.ipynb
# ---------------------

import sqlite3
import pandas as pd
'''
    pandas can read from HTML,JSON,SQL,EXCEL,HDF5,Stata, and a few other things.

    Read data from a SQL database using the pd.read_sql function.

    read_sql take 2 arguments: a SELECT statement, and s database connection object.

    This is great because it means you can read from any kind of SQL database,
    it doesn't matter if it's MySQL,SQLite,PostgreSQL,or something else.
'''

'''
    9.1 Reading data from SQL databases  读取数据
'''
con = sqlite3.connect('../data/weather_2012.sqlite')
df = pd.read_sql('select * from weather_2012 LIMIT 3', con, index_col='id')  # 设置id索引
# print df
df = pd.read_sql('select * from weather_2012 LIMIT 3', con, index_col=['id', 'date_time'])  # 设置双重索引
# print df

'''
    9.2 Writing to a SQLite database  写入数据
'''
# weather_df = pd.read_csv('../data/weather_2012.csv')
# con = sqlite3.connect('../data/test_db.sqlite')
# con.execute('drop table if exists weather_2012')
# weather_df.to_sql('weather_2012', con)

con = sqlite3.connect('../data/test_db.sqlite')
df = pd.read_sql('select * from weather_2012 LIMIT 3', con, index_col='index')
# print df

con = sqlite3.connect('../data/test_db.sqlite')
df = pd.read_sql('select * from weather_2012 order by Weather LIMIT 3', con)
print df

'''
    sqlite3 database:连接数据库-->sqlite3.connect()
    PostgreSQL database:连接数据库-->psycopg2.connect()
    MySQL database:连接数据库-->MySQLdb.connect()
'''

'''
    9.3 Connecting to other kinds of database
'''
import MySQLdb
con = MySQLdb.connect(host='localhost', db='test')

import psycopg2
con = psycopg2.connect(host='localhost')
