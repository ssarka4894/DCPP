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


from collections import deque

def print_sliding_window_max(arr, k):
    if k <= 0 or k > len(arr):
        print("Input Not Valid!")
        return

    dq = deque()  # will store indices, arr[dq] is decreasing

    for i, x in enumerate(arr):
        # 1) Remove indices that are out of the current window [i-k+1, i]
        while dq and dq[0] <= i - k:
            print("loop1", dq)
            dq.popleft()

        # 2) Maintain decreasing order in deque
        while dq and arr[dq[-1]] <= x:
            print("loop2", dq)
            dq.pop()

        dq.append(i)
        
        print("outside loop", dq)

        # 3) Output max once the first window is formed
        if i >= k - 1:
            print(arr[dq[0]], end=" " if i < len(arr) - 1 else "\n")

# Example
print_sliding_window_max([10, 5, 2, 7, 8, 7], 3)  # 10 7 8 8

    

