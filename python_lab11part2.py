# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:24:57 2021

@author: Cristian
"""
import pandas as pd

df = pd.read_csv('tb.csv')

#print(df)

tb_melt = pd.melt(df, id_vars=['country', 'year'])
#print(tb_melt.head())

#create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]
#print(tb_melt['gender'].str[0])

pd.set_option('display.max_rows', None, "display.max_columns", None, 'display.max_colwidth', None)

print(tb_melt)
