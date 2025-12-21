# -*- coding: utf-8 -*-
"""
Given the mapping a= 1, b = 2, ... , z = 26, and an encoded message, count the
number of ways it can be decoded.
For example, the message "111" should be 3, since it could be decoded as "aaa",
" ka", and "a k" .
You can assume that the messages are always decodable. For example, "001" is not
allowed.
"""

from collections import defaultdict

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


print("result: ", num_encodings('1111'))