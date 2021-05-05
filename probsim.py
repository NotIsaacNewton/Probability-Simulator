#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:21:04 2021

@author: ariandovald
"""
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import random as random

n_total = 0
p_win = 0.01
p_lose = 1 - p_win
t = 0
p = []
n_space = []
n = 1

# s = 0
# while n-1 <= 200:
#     m = 0.99**(n)
#     s += m
#     n += 1
# a = 1/(1-0.99)
# print((a-s)*0.0101010101)

while n <= 1000:
        n_space.append(n)
        p.append(np.log(p_win*(p_lose**(n-1))))
        n += 1
plt.plot(n_space, p, 'bo')
z = np.polyfit(n_space, p, 1)
slope, intercept = z
print(slope, intercept)

while t <= 10000:
    p = []
    n = 1
    while True:
        p.append(p_win*(p_lose**(n-1)))
        r = random.randint(0,100)
        if r == random.randint(0,100):
            break
        n += 1
    n_total += n
    t += 1

n_average = n_total * (t**(-1))
print(n_average)
    