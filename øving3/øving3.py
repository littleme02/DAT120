# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:13:55 2021

@author: LittleMe
"""

import turtle
import sys

layers = int(input("Layers to draw: "))
width = 10

turtle.clear()
turtle.colormode(255)

if layers <= 0: 
    print("Can't draw less than 1 layer")
    sys.exit()

turtle.speed(0)

for i in reversed(range(1,layers+1)):
    print(i)
    turtle.up()
    turtle.setpos([0*i,width*i])
    turtle.begin_fill()  
    turtle.down() 
       
    if(i % 2 == 0):turtle.fillcolor((255,255,255))

    else: turtle.fillcolor((0,0,0))
    
    turtle.setpos([width*i,0*i])
    turtle.setpos([0*i,-width*i])
    turtle.setpos([-width*i,0*i])
    turtle.setpos([0*i,width*i])
    
    turtle.end_fill()
    