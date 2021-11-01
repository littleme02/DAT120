# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:16:20 2021

@author: LittleMe
"""

import turtle

#turtle.speed(0)
turtle.screensize(400,5000)

while(True):
    for i in range(6):
        turtle.forward(80)
        turtle.right(60)
    turtle.up()
    turtle.setpos(turtle.position() + [0,139])
    turtle.down()
