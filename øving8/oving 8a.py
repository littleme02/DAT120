
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:58:11 2021

@author: LittleMe
"""

import sys


inputfilename = ""
word_dict = {}
sorted_dict = {}

inputfilename = input("Input file(empty for oving_1_rein_tekst.txt): ")
if inputfilename == "":
    inputfilename = "oving_1_rein_tekst.txt"

try:
    inputfile = open(inputfilename, mode="r", encoding="utf-8")
except: 
    print("U goofed, file you want must be in the folder")
    sys.exit()

index = 1

for line in inputfile:
    
    words = line.split()
    for word in words:
        if word.isalpha():
            word = word.capitalize()
            if word not in word_dict:
                word_dict[word] = [index]
            elif word in word_dict:
                word_dict[word].append(index)
                
    index += 1
    
sortedkeys = sorted(word_dict)

for key in sortedkeys:
    sorted_dict[key] = word_dict[key]
    
print(sorted_dict)
            
    
