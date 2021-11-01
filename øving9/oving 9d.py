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
    

inputfilename = "" #input("Input file(empty for sporsmaalsfil.txt): ") #Commented out for dev
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
    
    qustobs.append(question(line[0].strip(),line[2],int(line[1].strip())))
    
# for svar in qustobs:
#     print(svar.ask())
#     print(svar.korrekt_svar_teks()+ "\n")
    

if __name__ == "__main__" :
    
    p1score = 0
    p2score = 0
    p1ans = ""
    p2ans = ""
    
    for game in qustobs:
        
        print(game.ask())
        
        p1ans = int(input("Player 1: "))-1
        p2ans = int(input("Player 2: "))-1
        
        print("\n" + "Correct answer: " + game.korrekt_svar_teks().capitalize() + "\n" )
        if p1ans == game.answer:
            p1score += 1
            print("Player 1 Correct")
        else: 
            print("Player 1 BAD")
        
        if p2ans == game.answer:
            p2score += 1
            print("Player 2 correct")
        else: print("Player 2 BAD")
        print("\n")
        
        
    print("Player 1 score: " + str(p1score))
    print("Player 2 score: " + str(p2score))
    
    if p1score > p2score:        print("Player 1 wins")
    elif p1score < p2score:      print("Player 2 wins")
    elif p1score == p2score:     print("Draw")
    