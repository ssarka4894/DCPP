# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:21:34 2025

@author: soham
"""
            
import numpy as np
# defining a function with number of 
# total staircase steps: n
# set of possible step jumps: X, for example X = [1, 2]
def count_step(n, X):
    # defining a storage space to save memory
    storage = np.zeros(n + 1)
    # define default storage = 1
    storage[0] = 1
    # run a loop from 1 to n + 1
    for i in range(n + 1):
        # f(n) = f(n - X1) + f(n - X2) + ...
        for step in X:
            if i - step >= 0:
                storage[i] += storage[i - step]
    
    return int(storage[n])

# define number of total staircases n = 4 and set X = [1, 2]
print(count_step(4,[1,2]))
        

    

