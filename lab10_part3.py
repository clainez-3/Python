# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:46:23 2021

@author: Cristian
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("file_messy.csv")

print(df.head())

#print(df.head())

df2 = pd.read_csv('file_messy.csv', delimiter = ' ', header = None)

print(df2.head())

#df2.to_csv('file_clean.csv', index=False)

df2.to_csv('file_clean1.xlsx', index=False)
