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
aim = 0
depth = 0
horizontal = 0

for i in range(lineCount):
   cmdList = lineList[i].split()
   cmd = cmdList[0]
   change = int(cmdList[1])
   # print('cmd: ' + cmd + ' change: ' + str(change))
   if cmd == 'forward':
      horizontal = horizontal + change
      depth = depth + (aim * change)
   elif cmd == 'down':
      aim = aim + change
   elif cmd == 'up':
      aim = aim - change
   else:
      print('bad command')


print('depth: ' + str(depth) + ' horizontal: ' + str(horizontal))
print('depth x horizontal = ' + str(depth * horizontal))

print(str(lineCount) + ' lines processed')

inFile.close()      
