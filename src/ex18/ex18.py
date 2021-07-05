'''
Author: your name
Date: 2021-07-05 09:04:18
LastEditTime: 2021-07-05 09:14:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learn-Python3-the-Hard-Way\src\ex18\ex18.py
'''
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

'''
arg1:Zed,arg2:Shaw
arg1:Zed,arg2:Shaw
arg1:First!
I got nothin'.
'''