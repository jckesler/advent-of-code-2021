#!/usr/bin/python

import os
import sys

if len(sys.argv) < 2:
   print('syntax: ' + sys.argv[0] + ' <filename>')
   sys.exit()

filename = sys.argv[1]

inFile = open(filename, 'rb')
print('reading ' + filename)
lineList = inFile.readlines()
lineCount = len(lineList)
increaseCount = 0
window = [0 for i in range(lineCount - 2)]

w = 0
for i in range(lineCount):
   if i < lineCount - 2:
      x = int(lineList[i])
      y = int(lineList[i + 1])
      z = int(lineList[i + 2])
      window[w] = x + y + z
      w = w + 1     

for i in range(w - 1):
   if window[i] < window[i + 1]:
      increaseCount = increaseCount + 1

print('increases: ' + str(increaseCount))

print(str(lineCount) + ' lines processed')

inFile.close()      
