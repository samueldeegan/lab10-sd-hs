"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): 
    return a+b
def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by 0')
    else:
        return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0.")

    return math.log(b,a) # use math library + raise ValueError

def exp(a, b):
    return a**b



