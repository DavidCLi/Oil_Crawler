#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:29:46 2020

@author: david
"""

import pymysql

db = pymysql.Connect("localhost", "root", "1qaz@WSX", "HistoryGasPrice")
cursor = db.cursor()
sql    = "select * from HistoryGasPrice"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print("%s,%6.2f,%6.2f,%6.2f,%6.2f," % (row[0],row[1],row[2],row[3],row[4]))

except:
    print("Error: unable to fetch data")
    
db.close()
    
