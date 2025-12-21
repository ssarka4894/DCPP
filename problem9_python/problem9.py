# -*- coding: utf-8 -*-
"""
This problem was asked by Amazon. Given an integer k and a string s, 
find the length of the longest substring that contains at most k distinct
 characters. For example, given s =“abcba” and k = 2, the longest substring 
 with k distinct char- acters is “bcb”.
"""

from collections import defaultdict

def longest_substring_k_distinct(s: str, k: int) -> int:
    if k <= 0 or not s:
        return 0

    freq = defaultdict(int)
    left = 0
    best = 0

    for right, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:
            left_ch = s[left]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            left += 1
        best = max(best, right - left + 1)

    return best

print(longest_substring_k_distinct("abcba", 2))  # 3 ("bcb")