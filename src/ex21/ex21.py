'''
Author: your name
Date: 2021-07-05 15:01:54
LastEditTime: 2021-07-06 09:32:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learn-Python3-the-Hard-Way\src\ex21\ex21.py
'''
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a,b):
    print(f"DIVIDEING {a} / {b}")
    return a/b

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age:{age},Height:{height},Weight:{weight},IQ:{iq}")

'''
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDEING 100 / 2
Age:35,Height:74,Weight:180,IQ:50.0
'''