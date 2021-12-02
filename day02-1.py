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
depth = 0
horizontal = 0

for i in range(lineCount):
   cmdList = lineList[i].split()
   cmd = cmdList[0]
   change = int(cmdList[1])
   # print('cmd: ' + cmd + ' change: ' + str(change))
   if cmd == 'forward':
      horizontal = horizontal + change
   elif cmd == 'down':
      depth = depth + change
   elif cmd == 'up':
      depth = depth - change
   else:
      print('bad command')


print('depth: ' + str(depth) + ' horizontal: ' + str(horizontal))
print('depth x horizontal = ' + str(depth * horizontal))

print(str(lineCount) + ' lines processed')

inFile.close()      
