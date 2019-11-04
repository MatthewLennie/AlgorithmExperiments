# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:31:56 2019

@author: lennie
"""

from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
sampleA = np.mean([160+40*x**2 for x in poisson(0.88).rvs(1000000)])

sampleB = np.mean([128+40*y**2 for y in poisson(1.55).rvs(10000)])

print(sampleA)
print(sampleB)
#%%
expectA = 0
expectB = 0
cumProb = 0 
for i in range(0,1000):
    cumProb += poisson(0.88).pmf(i)
    expectA += poisson(0.88).pmf(i)*(160+40*i^2)
    expectB += poisson(1.55).pmf(i)*(128+40*i^2)
    
print(expectA/cumProb)
print(expectB)
 #%%

dist = poisson(3)
dist.cdf(1)
dist.pmf(0)

#Always look for the inverse case as a short cut
print(1-2*dist.pmf(1)*dist.pmf(0)+dist.pmf(0)*dist.pmf(0))

#%%

dist = poisson(1.2)
dist.cdf(2)
record = [] 
for i in range(1000000):
    record.append(sum(dist.rvs(40))>3)

np.mean(record)