# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:22:27 2021

@author: Cristian
"""
import matplotlib.pyplot as plt

lst_life_exp = [30, 40, 50, 60, 70, 80, 90]

lst_gdp_gap = [0, 10000, 20000, 30000, 40000, 50000, 60000]

# plt.plot(lst_gpd_gap, lst_life_exp)    Line chart

plt.scatter(lst_gdp_gap, lst_life_exp)

plt.show()