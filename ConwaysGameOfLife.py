# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:55:13 2019
Conways Game of Life 

Principles Learn:
    Sometimes you can't avoid the outer loop. 
    But you can store the infomation sparesly to save space 
    i.e. using a dictionary to just store the live cells. 
    
@author: matt_
"""

from numpy.random import choice
import itertools 
import matplotlib.pyplot as plt
#Random Initialize. 
import numpy as np
Grid = 100

active_cells = np.array([choice(range(Grid),Grid**2//2),choice(range(Grid),Grid**2//2)]).transpose()
active_dict = {}
for i in active_cells:
    active_dict[tuple(i)] = 1
    
coords = [x for x in itertools.product(range(Grid),repeat=2)]

neighbour_coords = [x for x in itertools.product(range(-1,2),repeat=2)]
next_dict = {}
f = plt.matshow(np.zeros([Grid,Grid]))
#%%
for rep in range(10):
    for coord_pair in coords:
        neighbours = 0
        
        for neighbour in neighbour_coords:
            current_inspection = tuple(np.array(coord_pair)+np.array(neighbour))
            #not going to optimize for border checking yet. 
            if neighbour != (0,0) and current_inspection in active_dict:
#                print("branch 1")
                neighbours+=1
            elif neighbour != (0,0):
#                print("branch 2")
                status = True #True means alive
        
        if status and neighbours>2 and neighbours <=3:
            next_dict[coord_pair] = 1
        elif not status and neighbours ==3:
            next_dict[coord_pair] = 1
    active_dict = next_dict
#    print(active_dict)
    next_dict={}

    Visualize(active_dict,Grid)
    
        
#%% visualize function 
def Visualize(status_dict, Grid):
    full_grid = np.zeros([Grid,Grid])
    for coord in status_dict:
        full_grid[coord]=1
    
    plt.gca().matshow(full_grid)
    
    
        