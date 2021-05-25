# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:17:17 2021

@author: Cristian
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#pd.set_option('display.max_rows', None, "display.max_columns", None, 'display.max_colwidth', None)


df_Sales = pd.read_csv("vgsalesclean2.csv")

#print(df_Sales)

#print(df_Sales['NA_Sales'].describe())

#print(df_Sales['EU_Sales'].describe())


#print(df_Sales['Global_Sales'].describe())

#print(df_Sales['JP_Sales'].describe())

#print(df_Sales.head())

#df = sns.load_dataset(df_sales)

#print(df.head())

#plt.scatter(df.speeding,df.alcohol)

#sns.set()

#sns.set_style("whitegrid")
#sns.set_style("dark")

#plt.show()