# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:56:24 2021

@author: Cristian
"""

import pandas as pd

ebola = pd.read_csv('ebola.csv')
#print(ebola)

#melt ebola : ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name = 'status_country', value_name = 'counts')

#print the head of ebola_melt
#print(ebola_melt.head())

status_country = ebola_melt['status_country']

#concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

#print the shape of ebola_tidy
print(ebola_tidy.shape)

#print the head of ebola_tidy
print(ebola_tidy.head())


