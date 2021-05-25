# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:01:44 2021

@author: Cristian
"""

import pandas as pd

airquality = pd.read_csv('airquality.csv')

#print the head of air quality
print(airquality.head())

#calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

#replace all missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

#print the info of airquality
print(airquality.info())
