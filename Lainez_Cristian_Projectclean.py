# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:17:17 2021

@author: Cristian
"""

import pandas as pd


df_sales = pd.read_csv("vgsales.csv")

pd.set_option('display.max_rows', None, "display.max_columns", None, 'display.max_colwidth', None)

#print(df_sales.head())

#print(df_sales['NA_Sales'].describe())

#print(df_sales['EU_Sales'].describe())


#print(df_sales['Global_Sales'].describe())

#print(df_sales['JP_Sales'].describe())

#print(df_sales.head())

df_sales['Global_Sales'].plot(kind = 'box')

#mean = df_sales.mean(axis = 'columns') 
#mean.plot() 

#print('Mean Value:',df_sales['NA_Sales'].mean()) 

#print('Standard Deviation Value:',df_sales['EU_Sales'].std())



