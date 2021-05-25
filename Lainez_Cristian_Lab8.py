# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:03:59 2021

@author: Cristian
"""
import pandas as pd
 
df = pd.read_csv("world_population.csv")
 
#print(df)

new_labels = ('Year of Population', 'World Population')

#integrate new labels 
df2 = pd.read_csv("world_population.csv", header = 0, names= new_labels)

print(df2)