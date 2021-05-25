# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:18:37 2021

@author: Cristian
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('temp.csv')

df.plot(color = 'red')

plt.title('Temperature Values')

plt.xlabel('')#to specficy something in the X axis

plt.ylabel('Index')#y-axis
 
plt.show()

