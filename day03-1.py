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
numBits = len(lineList[0]) - 1

gamma = 0
epsilon = 0
for i in range(numBits):
   num0 = 0
   num1 = 1
   for j in range(lineCount):
      bit = lineList[j][i]
      if bit == '0':
         num0 = num0 + 1
      elif bit == '1':
         num1 = num1 + 1
      if num1 > num0:
         gammaBit = 1
         epsilonBit = 0
      else:
         gammaBit = 0
         epsilonBit = 1
   print "column " + str(i) + " gamma " + str(gammaBit) + " epsilon " + str(epsilonBit)
   gamma = gamma + (gammaBit * (2 ** (numBits - i - 1)))
   epsilon = epsilon + (epsilonBit * (2 ** (numBits - i - 1)))

powerConsumption = gamma * epsilon
print "gamma " + str(gamma) + " epsilon " + str(epsilon)
print "power consumption " + str(powerConsumption)
      
print(str(lineCount) + ' lines processed')

inFile.close()      
