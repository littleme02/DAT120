# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:58:11 2021

@author: LittleMe
"""

import sys
import re

regmatch = re.compile("(?<=\<)(.*?)@(.*?)(?=\>)|(?<=mailto:)(.*?)@(.*?)(?=\])")


inputfilename = input("Input file(empty for hadoop_1m.txt): ")
if inputfilename == "":
    inputfilename = "hadoop_1m.txt"

try:
    inputfile = open(inputfilename)
except: 
    print("U goofed, file you want must be in the folder")
    sys.exit()

try:
    outputfile = open(input("Output file: "),"x")
except: 
    print("U goofed, prolly already is a thing or not valid filename")
    sys.exit()

for line in inputfile:
    line.strip()
         
    if (line.find("From: ") != -1):
        match = re.search(regmatch, line)
               
        if match:
            email = match[0]
            outputfile.write(email + "\n")
        else:
            match = re.search("\S+@\S+\.\S+$", line)
            if match:
                email = match[0]
                outputfile.write(email + "\n")
            else:
                print("Error with: " +line)
            