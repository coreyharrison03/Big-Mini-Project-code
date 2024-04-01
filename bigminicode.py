# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:52:59 2024

@author: corey
"""

import numpy as np
import random


n=5

def attack_randomtwo(circle):#fills glasses completely randomly, used to test the efficiency of defence strategies
    
    placements = np.arange(n)
    
    fill = random.choice(placements)
    amount = random.uniform(0,0.5)
    
    circle[fill]+=amount
    placements = np.delete(placements, fill)
    fill = random.choice(placements)
    amount = 0.5 - amount
    circle[fill]+=amount
    return circle

def attack_truerandom(circle):
    amounts = np.random.rand(n)
    total = 0
    for i in amounts:
        total += i
    div = 2*total
    amounts = amounts / div
    for i in range (n):
        circle[i] += amounts[i]
        
    return circle
    
def defense_random(circle):
    nonzerocircle = circle[circle != 0]
    placements = np.arange(len(nonzerocircle))
    
    empty = random.choice(placements)
    circle[empty] = 0
    
    if circle[(empty-1) % n] > circle[(empty+1) % n]:
        circle[(empty-1) % n] = 0
    else: 
        circle[(empty+1) % n] = 0
    return circle
    
def defense_random_bad(circle):#empties random glasses that have value >0 for testing the efficiency of attack strategies
    nonzerocircle = circle[circle != 0]
    placements = np.arange(len(nonzerocircle))
    
    empty = random.choice(placements)
    direction = np.random.randint(0,2) * 2 - 1
    circle[empty] = 0
    empty = (empty + direction) % n
    circle[empty] = 0
    return circle

def attack_evenrandom(circle):
    amounts = np.random.rand(n//2)
    total = 0
    for i in amounts:
        total += i
    div = 2*total
    amounts = amounts / div
    for j in range (len(amounts)):
        circle[2*j-1] += amounts[j-1]
        
    return circle

def defense_highhigh(circle):#finds the highest value in the circle and deletes it then deletes whichever of its neighbours is greater
    high=0
    for i in range(len(circle)):
        if circle[i] > circle[high]:
            high = i

    circle[high] = 0
    
    if circle[(high-1) % n] > circle[(high+1) % n]:
        circle[(high-1) % n] = 0
    else: 
        circle[(high+1) % n] = 0
    return circle
    
  
circle = attack_randomtwo(np.zeros(n))
attackwin = False
for i in range(10000000):
    circle = defense_highhigh(circle)
    circle = attack_randomtwo(circle)
    if np.max(circle) > 1:
        attackwin = True
        break

if attackwin:
    print("Attack wins" + " after " + str(i+1) + " rounds!")
else:
    print("Defense wins!")
