# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#open the text file
try:
  fhand = open('mbox2.txt')
except:
  print("File cannot be opened")

#print the number of lines in the file that start with the word subject
count = 0
for line in fhand:
    if line.startswith('Subject:'):
      count = count + 1         
print("Line Count", count)

