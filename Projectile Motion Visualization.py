# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 05:10:40 2020

@author: farhad324
"""
import easygui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

## Easy GUI ##

msg = "Enter velocity & angle"
title = "Input for projectile simulation"
fieldNames = ["Velocity","Angle"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg,title, fieldNames)
print(fieldValues)

while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
print ("Reply was:", fieldValues)

## Matplotlib Animation ##
sns.set()
fig, ax = plt.subplots()
g = 9.81                                                       #value of gravity
v = float(fieldValues[0])                                      #initial velocity
theta = float(fieldValues[1])  * np.pi / 180.0                 #initial angle of launch in radians
t = 2 * v * np.sin(theta) / g
r_for_h= v*np.cos(theta)*(t/2)
h=((v**2) *(np.sin(theta)**2))/(2*g)
r= (v**2) * np.sin(2*theta) / g
time_text="Flight Time: "+str(round(t,2))+'s'  
h_point="Highest Point: "+str(round(h,2))+'m'
range_projectile="Range: "+str(round(r,2))+'m'
plt.plot(r,0,'go')
plt.plot(r_for_h,h,'ro')
plt.text(r_for_h+1, h+1, h_point) 
plt.text(r+1, 1, range_projectile)  
plt.text(r_for_h+1, h+2.5, time_text) 

                            
t = np.arange(0, 0.1, 0.01)                                    #time of flight into an array
x = np.arange(0, 0.1, 0.01)
line, = ax.plot(x, v * np.sin(theta) * x - (0.5) * g * x**2)   # plot of x and y in time

def animate(i):
    """change the divisor of i to get a faster (but less precise) animation """
    line.set_linestyle("-")
    line.set_linewidth(3.5)                  
    line.set_xdata(v * np.cos(theta) * (t + i /100.0))
    line.set_ydata(v * np.sin(theta) * (x + i /100.0) - (0.5) * g * (x + i / 100.0)**2)
    return line,
 

plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('Distance (x)')
plt.ylabel('Distance (y)')
plt.axis([-1.0, 25.0, -0.5, 8.0])
ax.set_autoscale_on(False)

ani = animation.FuncAnimation(fig, animate,frames=np.arange(1, 200),interval=20)
plt.show()
