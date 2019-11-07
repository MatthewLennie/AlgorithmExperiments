# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:43:37 2019
Triple STep 
Just accumlate the probabilities as you move along the stairs. 

I assume that you didn't need to exactly meet the step, This just changes how we 
handle the last iterations
It appears that there is a closed form solution to this problem, it is very neat
when you write out the steps. I couldn't immediately find the closed form solution
however
@author: matt_
"""
import numpy as np
 
Steps = [1,2,3]

n = 1



scores = [1,1,1,0]
Position = 0
for i in range(n):
    current = scores.pop(0)
    scores = [current + x for x in scores]
    scores.append(0)
print(sum(scores))    
        
    
#%%

    