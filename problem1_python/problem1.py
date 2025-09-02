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

KInput = int(input('Enter any number: '))

n = len(ListInput)

def checkEqual(ListInput, KInput, n):
    
    for i in range(n):
        for j in range(n):
            sum = 0
            if j >= i:
                sum = int(ListInput[i]) + int(ListInput[j])
                if sum == KInput:
                    return True
    

if checkEqual(ListInput, KInput, n) == True:
    print("True")
    
else:
    print("False")

