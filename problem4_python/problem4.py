# -*- coding: utf-8 -*-
"""
Created on Tue May 14 03:09:30 2024

@author: soham
"""

print("Enter any two numbers: \n")

a = input('Enter the first number \n')
b = input('Enter the second number \n')

class cons:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.f = [self.a, self.b]
        

pair = cons(a,b)
    
def car(pair):
    return pair.a

def cdr(pair):
    return pair.b


# run in terminal
# cdr(pair)

# car(pair)


output1= cdr(cons(1,2))

output2= car(cons(1,2))

print('cdr output',output1)

print('car output',output2)

