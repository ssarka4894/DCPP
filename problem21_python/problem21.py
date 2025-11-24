# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 20:32:21 2025

@author: soham

This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number
of ways it can be decoded.
For example, the message ’111’ would give 3, since it could be decoded as ’aaa’, ’ka’,
and ’ak’.
You can assume that the messages are decodable. For example, ’001’ is not allowed.

"""

import re
import numpy as np

# Get input from user
ListInput  =  input('Enter your message:')
# Print the user input for verification
print('Here is your message', ListInput)

# Let's store the input as an array
b = np.array(ListInput, dtype = int)
n = len(ListInput)
i = 0
a = np.zeros(n)

while (b!=0):
    r = b % 10
    a[i] = r
    b = int(b/10)
    i = i + 1
    


