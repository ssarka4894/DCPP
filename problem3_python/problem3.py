"""
# Created by:
##################################
#########SOHAM SARKAR#############
#####Arizona State University#####
##################################

# Do NOT distribute without written permission from Soham Sarkar
# Do NOT use it for any commercial purpose

# Contact email: ssarka30@asu.edu
# Last update: July 19, 2023
"""

import re

ListInput  = list(map(int, re.findall(r"[-+]?\d+", input('Enter your list of elements:'))))
print('Here is your entered list', ListInput)

n = len(ListInput)


def find_lowest_positive_integer(InputArray, length):
    output = 1
    counter = 1
    for i in range(length):
        if InputArray[i] > 0:
            if counter in InputArray:
                counter += 1
            output = counter
    return output


digit = find_lowest_positive_integer(ListInput,n)
print("Lowest Positive Integer: ", digit)