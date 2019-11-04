# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:55:47 2019
Implementation of the Robot in a Grid Problem 
Didn't really see the advantage of programming this recursively. 
I just use a stack to implement a depth first search with a hash table 
to record the already visited and blocked cells. 
@author: matt_
"""
import numpy as np
from itertools import product
r = 500000
c = 300000
Blocked = {(1,1):0,(2,1):0, (3,1):0}
Goal = [c,r]
visited = {}
to_visit = [np.array([0,0])]
def IsLegal(proposed_moves,r,c,Blocked,Visited):
    legal_moves = []
    for move in proposed_moves:
        if all(move>=0) and move[0]<=r and move[1]<=c and tuple(move) \
        not in Blocked and tuple(move) not in Visited:
            legal_moves.append(move)
    return legal_moves

def GenNewMoves(Current,r,c,Blocked,Visited):
    new_moves = []
    for row,col in product(range(-1,2),repeat=2):        
        new_moves.append(Current+np.array([row,col]))
    
    return IsLegal(new_moves,r,c,Blocked,Visited)
#%%
solved = False
while to_visit:    
    current = to_visit.pop()
    if all(current ==np.array([r,c])):
        print("solved: {}".format(current))
        solved = True
        break
    visited[tuple(current)] = 0
    to_visit.extend(GenNewMoves(current,r,c,Blocked,visited))
    
