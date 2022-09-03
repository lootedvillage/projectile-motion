# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:31:09 2021

@author: Tom
"""

# This is a program to calculate the kinetic & potential components of the energy of a falling projectile

import numpy as np
import matplotlib.pyplot as plt

# Defining the arrays we will need to store the relevant data

timeData = np.linspace(0.0, 4.5, num=50)
heightData = []
kineticEnergyData = []
potentialEnergyData = []
totalEnergyData = []

# Defining the constants of the motion

# m = mass of the projectile in kilograms
m = 1.0

# g = acceleration due to gravity in metres per second squared
g = 9.81

# Creating the functions we will need in order to do the calculations

# Function that calculates the vertical hieght of the projectile at time t
def heightCalc(t):
    temp_t = t
    h = 100.0 - (0.5 * g * temp_t * temp_t)
    return(h)

# Function that calculates the velocity of the projectile at time t
def velocityCalc(t):
    temp_t = t
    vel = -g * temp_t
    return(vel)

# Function that calculates the potential energy of the projectile at time t
def potentialEnergyCalc(h):
    temp_h = h
    V = m * g * temp_h
    return(V)

# Function that calculates the kinetic energy of the projectile at time t
def kineticEnergyCalc(v):
    temp_v = v
    T = 0.5 * m * temp_v * temp_v
    return(T)

    
# This loop calculates and then stores the energy values over the course of the motion
for i in range(len(timeData)):
    temp_height = heightCalc(timeData[i])
    heightData.append(temp_height)
    temp_vel = velocityCalc(timeData[i])
    
    temp_PE = potentialEnergyCalc(temp_height)
    potentialEnergyData.append(temp_PE)
    temp_KE = kineticEnergyCalc(temp_vel)
    kineticEnergyData.append(temp_KE)
    
    temp_TE = temp_PE + temp_KE
    totalEnergyData.append(temp_TE)

# Plotting the relevant data
plt.plot(timeData, kineticEnergyData, "g")
plt.plot(timeData, potentialEnergyData, "r")
plt.plot(timeData, totalEnergyData, "b")
plt.title("Energy of a Falling Projectile Falling from Rest")
plt.xlabel("time (s)")
plt.ylabel("Energy (J)")
plt.legend(["Green - Kinetic Energy", "Red - Potential Energy", "Blue - Total Energy"])
plt.show()
    
    
    
    
    
    