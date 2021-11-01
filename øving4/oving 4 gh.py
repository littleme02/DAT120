# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:35:09 2021

@author: LittleMe
"""

import math


def xydist(x,y):
    if x < 0: x = -x
    if y < 0: y = -y
    return(math.sqrt(x**2+y**2))


def pointdist(x1,y1,x2,y2):
    x2 -= x1
    y2 -= y1
    return xydist(x2,y2)
    


try:
    a = float(input("pointx1: "))
    b = float(input("pointy1: "))
    c = float(input("pointx2: "))
    d = float(input("pointy2: "))
    print(pointdist(a,b,c,d))
   
except: print("Error")