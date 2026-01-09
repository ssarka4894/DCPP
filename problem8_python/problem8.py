# -*- coding: utf-8 -*-
"""

This problem was asked by Google.
Given an array of integers and a number k, where 1 ≤ k ≤ length of the array, compute
the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8],
since:
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you
do not need to store the results. You can simply print them out as you compute them.

@author: soham
"""


def computeMaxSubArray(userInput, k):
    # if length of userinput is 0, it should return 0.
    if(len(userInput) == 0):
        print("Input Not Valid!")
        return 0
    
    index = 0
    store = [] # stores max values of subarrays
    for elem in userInput:
        findmax = [] # stores subarrays
        count = 0 # keep counter as 0
        if (index + k > len(userInput)):
                break
        while (count < k):
            findmax.append(userInput[count + index])
            count = count + 1
        # print(findmax)
        store.append(max(findmax))
        # print("elem", elem)
        index = index + 1
    return store
    
    
sol = computeMaxSubArray([10, 5, 2, 7, 8, 7], 3)
print("Solution =", sol)
        
    

