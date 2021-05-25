# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:07:12 2021

@author: Cristian
"""

import pandas as pd

# Read in the file: data frame 1

airquality = pd.read_csv('airquality.csv')

#print(airquality)

#Print the head of airquality (first few rows)
#print(airquality.head())

#melt function to apply a pivot type structure to results
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'])

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 100)
pd.set_option('display.width', None)



print(airquality_melt)