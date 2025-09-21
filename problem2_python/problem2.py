"""
# Created by:
##################################
#########SOHAM SARKAR#############
#####Arizona State University#####
##################################

# Do NOT distribute without written permission from Soham Sarkar
# Do NOT use it for any commercial purpose

# Contact email: ssarka30@asu.edu
# Last update: June 20, 2023
"""


import re

ListInput  = list(map(int, re.findall(r"[-+]?\d+", input('Enter your list of elements:'))))
print('Here is your entered list', ListInput)

n = len(ListInput)


def return_product_list(InputArray, length):
    
    output = []
    
    for i in range(length):
        mul = 1
        for j in range(length):
            if i!=j :
                mul = mul*InputArray[j]
        output.append(mul)
    return output


return_product_list(ListInput,n)