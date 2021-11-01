# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:25:06 2021

@author: LittleMe
"""

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
    
    



s1 = question("what?",["test1","this one","test3","test4"],2)
s2 = question("what?",["test1","test2","test3","this one"],4)

print(s1.ask())

a = int(input("Type answer number: "))
print("\n")
print(s1.Sjekk_svar(a))
print("\n")
print(s2.ask())

a = int(input("Type answer number: "))
print("\n")
print(s2.Sjekk_svar(a))