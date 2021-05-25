# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:35:08 2021

@author: Cristian
"""

import pandas as pd

ebola = pd.read_csv('ebola.csv')
#print(ebola)

#melt ebola : ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name = 'type_country', value_name = 'counts')

#print the head of ebola_melt
#print(ebola_melt.head()) 

#create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

#print(ebola_melt['str_split'])

#create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

#create the 'country' column 
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

#print the head of ebola_melt
print(ebola_melt.head())