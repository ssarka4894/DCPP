# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 02:40:06 2025

@author: soham
"""

from collections import defaultdict



# def num_encodings(s, total=0):
#     # There is no valid encoding if the string starts with 0.
#     if s.startswith('0'):
#         return 0
#     # Both the empty string and a single character should return 1.
#     elif len(s) <= 1:
#         return 1
#     total+= num_encodings(s[1:])
#     if int(s[:2]) <= 26:
#         total+= num_encodings(s[2:])
#     return total


def num_encodings(s):
    cache= defaultdict(int)
    cache[len(s)] = 1
    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            cache[i] += cache[i + 1]
            if int(s[i:i + 2]) <= 26:
                cache[i] += cache[i + 2]
    return cache[0]

value = num_encodings("111")
print(value)