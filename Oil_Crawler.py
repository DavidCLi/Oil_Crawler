#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:13:27 2020

@author: david
"""

from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import pymysql

def getData(url):
    try:
        html = requests.get(url).text
    except HTTPError as e:
        print(e)
        return None
    
    try:
        obj = BeautifulSoup(html,"html.parser")
        myList = []
        myData = obj.find_all('table', attrs={'id':'MyGridView'})
        myRows = myData[0].find_all('tr')
        
        for r in myRows:
            c = r.find_all('td')
            
            if( len(c) > 0         and
                len(c[0].text.replace("\n", "")) > 0 and 
                len(c[1].text.replace("\n", "")) > 0 and 
                len(c[2].text.replace("\n", "")) > 0 and 
                len(c[3].text.replace("\n", "")) > 0 and 
                len(c[4].text.replace("\n", "")) > 0 ):
                dataList = []
                dataList.append(c[0].text.replace("\n", "").split()[0])
                dataList.append(c[1].text.replace("\n", ""))
                dataList.append(c[2].text.replace("\n", ""))
                dataList.append(c[3].text.replace("\n", ""))
                dataList.append(c[4].text.replace("\n", ""))
                
                myList.append(dataList)
        
    except AttributeError as e:
        print(e)
        return None
    
    return myList

# Get Data from source 
mList = getData('https://vipmember.tmtd.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx')
# print(mList);
#Database connection
conn = pymysql.Connect("localhost", "root", "1qaz@WSX", "HistoryGasPrice")
cursor = conn.cursor()

for data in mList:
    sql = "insert into HistoryGasPrice values('{}', {}, {}, {}, {});".format(data[0], data[1], data[2], data[3], data[4])
    cursor.execute(sql);
    conn.commit()

conn.close()    
print('ok')

