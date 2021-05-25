# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:43:28 2021

@author: Cristian
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('car.csv')

print(df['distance traveled'].min())

print(df['distance traveled'].max())

#summary statistics 
print(df['distance traveled'].describe())