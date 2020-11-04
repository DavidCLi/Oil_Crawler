#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:29:46 2020

@author: david
"""

import pymysql
import matplotlib.pyplot as plt

db = pymysql.Connect("localhost", "root", "1qaz@WSX", "HistoryGasPrice")
cursor = db.cursor()
sql    = "select * from HistoryGasPrice"

try:
    listMonth = []
    listGas92 = []
    listGas95 = []
    listGas98 = []
    listGasW  = []
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        listMonth.append(row[0])
        listGas92.append(row[1])
        listGas95.append(row[2])
        listGas98.append(row[3])
        listGasW.append(row[4])
        #print("%s,%6.2f,%6.2f,%6.2f,%6.2f," % (row[0],row[1],row[2],row[3],row[4]))

except:
    print("Error: unable to fetch data")
    
db.close()

#draw
plt.figure(num = None, figsize = (3,3), dpi = 168, facecolor = 'w', edgecolor = 'k' )
plt.plot(listMonth, listGas92, label = "92")
plt.plot(listMonth, listGas95, label = "95")
plt.plot(listMonth, listGas98, label = "98")
plt.plot(listMonth, listGasW,  label = "W")
plt.xlabel('Month')
plt.ylabel('Dollors')
plt.legend()
plt.title('Python Data Science')    
plt.show()