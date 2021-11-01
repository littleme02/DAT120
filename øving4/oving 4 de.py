# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:06:19 2021

@author: LittleMe
"""

def kienergy(m, v):
    return((m*v^2)/2)


mass = input("Mass: ")
vel = input("Velocity: ")

try:
    print(kienergy(int(mass), int(vel)))
except: print("Error")