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
oxygenReading = []
co2Reading = []

def findOxygen(readingsList, bitPos):
   newList = []
   numBits = len(readingsList[0]) - 1
   if (bitPos == numBits) or (len(readingsList) == 1):
      return readingsList
   else:
      numReadings = len(readingsList)
      num0 = 0
      num1 = 0
      for i in range(numReadings):
         bit = readingsList[i][bitPos]
         if bit == '0':
            num0 = num0 + 1
         elif bit == '1':
            num1 = num1 + 1
      if num0 == num1:
         target = '1'
      elif num0 > num1:
         target = '0'
      else:
         target = '1'
      for i in range(numReadings):
         bit = readingsList[i][bitPos]
         if bit == target:
            newList.append(readingsList[i])
   readingsList = findOxygen(newList, bitPos + 1)
   return readingsList 

def findCO2(readingsList, bitPos):
   newList = []
   numBits = len(readingsList[0]) - 1
   if (bitPos == numBits) or (len(readingsList) == 1):
      return readingsList
   else:
      numReadings = len(readingsList)
      num0 = 0
      num1 = 0
      for i in range(numReadings):
         bit = readingsList[i][bitPos]
         if bit == '0':
            num0 = num0 + 1
         elif bit == '1':
            num1 = num1 + 1
      if num0 == num1:
         target = '0'
      elif num0 < num1:
         target = '0'
      else:
         target = '1'
      for i in range(numReadings):
         bit = readingsList[i][bitPos]
         if bit == target:
            newList.append(readingsList[i])
   readingsList = findCO2(newList, bitPos + 1)
   return readingsList 

reading = findOxygen(lineList, 0)
binaryStr = str(reading[0]).strip()
oxygen = int(binaryStr, 2)
print "oxygen binary " + binaryStr + " decimal " + str(oxygen)

reading = findCO2(lineList, 0)
binaryStr = str(reading[0]).strip()
co2 = int(binaryStr, 2)
print "co2 binary " + binaryStr + " decimal " + str(co2)

lifesupport = oxygen * co2
print "lifesupport rating " + str(lifesupport)
      
print(str(lineCount) + ' lines processed')

inFile.close()      
