# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:58:11 2021

@author: LittleMe
"""

import sys
import matplotlib.pyplot as plt

date = []
time = []
presbar = []
presabs = []
temp = []

inputfilename = ""

inputfilename = input("Input file(empty for trykk_og_temperaturlogg.csv): ")
if inputfilename == "":
    inputfilename = "trykk_og_temperaturlogg.csv"

try:
    inputfile = open(inputfilename)
except: 
    print("U goofed, file you want must be in the folder")
    sys.exit()

index = 0

for line in inputfile:
    if index != 0:
        line.strip()
        splitline = line.split(";")
        date.append(splitline[0])
        time.append(int(splitline[1]))
        if splitline[2] != "": presbar.append(float(splitline[2].replace(',','.')))
        presabs.append(float(splitline[3].replace(',','.')))
        temp.append(float(splitline[4].replace(',','.')))
    index += 1


print("Loaded")


plt.subplot(2,5,(1,3))
plt.plot(time[:], presabs[:])
plt.ylabel('kpa')
plt.grid(True)
plt.xticks(visible=False)

plt.subplot(2,5,(6,8))
plt.plot(time[:], temp[:])
plt.ylabel('temp')
plt.grid(True)

plt.xticks(rotation='vertical')

plt.subplot(2,5,(5,10))
num_bins = 20
n, bins, patches = plt.hist(temp, num_bins, facecolor='red', alpha=0.8)
plt.grid(True)

plt.show()
    
print("Plotted")

length = len(time)
for i in range(1,length):
    if time[i] != (time[i-1]+10):
        print(str(time[i]) + " and " + str(time[i-1]) + " is not 10 appart")