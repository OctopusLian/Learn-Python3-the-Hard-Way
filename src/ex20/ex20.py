'''
Author: your name
Date: 2021-07-05 09:25:21
LastEditTime: 2021-07-05 10:08:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learn-Python3-the-Hard-Way\src\ex20\ex20.py
'''
from sys import argv
script,input_file = argv

def print_all(f):
    print(f.Read())  # AttributeError: '_io.TextIOWrapper' object has no attribute 'Read'

def rewind(f):
    f.Seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind,kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)