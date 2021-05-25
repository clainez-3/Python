# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:47:52 2021

@author: Cristian
"""

import pandas as pd 

uber1 = pd.read_csv('nyc_uber_april.csv')

uber2 = pd.read_csv('nyc_uber_may.csv')

uber3 = pd.read_csv('nyc_uber_june.csv')

#concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1, uber2, uber3])

# print the shape of row_concat
print(row_concat.shape)

row_concat.dropna()

pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.max_colwidth', None)

# Print the head of row_concat
print(row_concat)