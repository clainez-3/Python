# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 20:42:30 2021

@author: Cristian
"""

fout = open('output.txt', 'w')
print (fout)

line1 = 'This is Summer, \n'
fout.write(line1)

line2 = 'Summer is my favorite weather. \n'
fout.write(line2)

fout.close()
