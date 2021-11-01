# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:47:24 2021

@author: Little-think
"""

while(True):
    try:
        if (int(input("heigth in cm: ")) >= 120):
            print("Yes go")
        else:
            print("No go")
        break
    except:
        print("invalid entry")
        