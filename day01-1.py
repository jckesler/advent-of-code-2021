#!/usr/bin/python

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

for i in range(lineCount):
   if i < lineCount - 1:
      x = int(lineList[i])
      y = int(lineList[i + 1])
      if y > x:
         increaseCount = increaseCount + 1

print('increases: ' + str(increaseCount))

print(str(lineCount) + ' lines processed')

inFile.close()      
