# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:01:34 2019

@author: lennie
"""

from numpy.random import uniform
from scipy.stats import norm, truncnorm
from numpy.random import choice
from numpy.random import normal 
import numpy as np
import matplotlib.pyplot as plt
Dist = normal(2.4,2.0)

Dist = norm(loc=2.4,scale=2.0)

my_clip_a = 0
my_clip_b = 250
loc = 2.4
scale = 2.0
a, b = (my_clip_a - loc) / scale, (my_clip_b - loc) / scale

truncnorm.pdf(num, a, b, loc, scale)


t_norm = truncnorm(a, b, loc, scale)

t_norm = truncnorm(a, b, loc, scale)
means = []

for i in range(10000):
#    num = choice(range(250),100)
#    normalize = 0
#    Summation = 0
#    
#    Summation = sum(t_norm.pdf(num)*num)
#    normalize = sum(t_norm.pdf(num))
#    means.append((Summation/normalize))
    means.append(np.sum(t_norm.rvs(100))<250)


sum(means)/len(means)
#%%
my_clip_a = 250
my_clip_b = 250
loc = 2.4
scale = 2.0
a, b = (my_clip_a - loc) / scale, (my_clip_b - loc) / scale

truncnorm.pdf(num, a, b, loc, scale)


t_norm = truncnorm(a, b, loc, scale)
