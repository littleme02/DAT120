# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:11:24 2021

@author: LittleMe
""" 
import math


def xydist(x,y):
    if x < 0: x = -x
    if y < 0: y = -y
    return(math.sqrt(x^2+y^2))
