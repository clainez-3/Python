# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 21:51:59 2021

@author: Cristian
"""

import matplotlib.pyplot as plt

lst_pop = []

for i in range(5):
    lst_pop.append(1)

#print(lst_pop)

lst_year = [2010, 2011, 2012, 2013, 2014]

#print(1st_year[-1])

plt.plot(lst_year, lst_pop)

plt.show()

