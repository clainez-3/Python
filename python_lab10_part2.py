# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:36:45 2021

@author: Cristian
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

print(df)

print(df['Fare'].describe())

#print(df['Fare'].mean())

#print(df['Fare'].std())

df['Fare'].plot(kind = 'box')

plt.show()