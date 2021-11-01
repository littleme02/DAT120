# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 11:51:03 2021

@author: LittleMe
"""
    
import sys
import re

class question:
    def __init__(self, quest, alts, answer):
        self.question = quest
        self.alternatives = alts
        self.answer = answer
    
    def ask(self):
        q = ""
        a = 1
        for i in self.alternatives:
            q = q + str(a)+ ": " + i + "\n" 
            a += 1        
        return(self.question + "\n" + q)
    
    def Sjekk_svar(self, a):
        return(a == self.answer)
    
    def korrekt_svar_teks(self):
        return(self.alternatives[int(self.answer)])
    

inputfilename = "" #input("Input file(empty for sporsmaalsfil.txt): ")
if inputfilename == "":
    inputfilename = "sporsmaalsfil.txt"

try:
    inputfile = open(inputfilename, mode="r", encoding="utf-8")
except: 
    print("U goofed, file you want must be in the folder")
    sys.exit()

qustobs = []
for line in inputfile:
    line = line.split(":")
    templist = []
    line[2] = re.findall("\w+", line[2])
    
    qustobs.append(question(line[0].strip(),line[2],line[1].strip()))
    
for svar in qustobs:
    print(svar.ask())
    print(svar.korrekt_svar_teks()+ "\n")
    

if __name__ == "__main__" :
    print("done")