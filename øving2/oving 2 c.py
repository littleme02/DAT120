# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:56:30 2021

@author: Little-think
"""
num = 0
inp = 0

while(True):
    inp = int(input("number please: "))
    
    if inp >= 0: num = num+inp
    else: break

print (num)