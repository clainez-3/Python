# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:29:59 2021

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

#sns.lmplot(x="NA_Sales", y = 'EU_Sales', data=df_Sales)

#sns.lmplot(x="", y = 'Global_Sales', data=df_Sales,
           #fit_reg = False,
           #)
#stats_df_Sales = df_Sales.drop(['Rank', 'Year', 'Genre','Publisher','Platform'], axis=1)
#sns.boxplot(data=stats_df_Sales)
#sns.boxplot(data=df_Sales)


#print(df.head())

#plt.scatter(df.speeding,df.alcohol)

#sns.set()

#sns.set_style("whitegrid")
#sns.set_style("dark")

#plt.show()

heatmap = df_Sales.corr()

sns.heatmap(heatmap)
