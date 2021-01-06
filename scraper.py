# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:45:35 2020

@author: KORHAN.KOZ
"""

import pandas as pd
import numpy as np
import requests

import csv

from bs4 import BeautifulSoup as bs

#reading the notebook file into a list.
companyandlinksList = list()
filepath = 'C:/Users/KORHAN.KOZ/Desktop/companyandlinks.txt'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       companyandlinksList.append(line.strip())
       line = fp.readline()


totalYearCol = list()
totalNameCol = list()
totalRevCol = list()

#Using the list and getting compname and url info for each comp.       
for company in companyandlinksList:
    tempstr = company.split(',')
    compname=tempstr[0]
    url = tempstr[1]
    print(url)
    r = requests.get(url)

    soup = bs(r.content, 'html.parser')
    table = soup.find('table', class_ = 'historical_data_table table')

    tbody = table.find('tbody')

    tempYearsCol = list()
    tempRevCol = list()
    tempNameCol = list()
    
    for row in tbody.find_all('tr'):
      tempYearsCol.append(row.find_all('td')[0].text)
      tempRevCol.append(row.find_all('td')[1].text)
    
    
    for i  in range(len(tempYearsCol)):
        tempNameCol.append(compname)
    
    print(len(tempNameCol),len(tempYearsCol))
    print(tempYearsCol,tempNameCol)
    
    totalYearCol.extend(tempYearsCol)
    totalNameCol.extend(tempNameCol)
    totalRevCol.extend(tempRevCol)
        

YearsColumn = np.asarray(totalYearCol)
RevColumn = np.asarray(totalRevCol)
NameColumn = np.asarray(totalNameCol)

datakk = {'Company Name': NameColumn,
        'Year': YearsColumn,
        'Revenue': RevColumn
        }
#writing the results in a csv file.
resultdf = pd.DataFrame(datakk, columns = ['Company Name','Year','Revenue'])
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1550)
pd.set_option('display.max_colwidth', 15000)
print(print(resultdf.head(150)))

resultdf.to_csv(r'C:/Users/KORHAN.KOZ/Desktop/GameCompRevF.csv')





    
    

    

