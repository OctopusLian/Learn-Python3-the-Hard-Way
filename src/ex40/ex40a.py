'''
Author: your name
Date: 2021-07-06 11:57:34
LastEditTime: 2021-07-06 13:50:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Learn-Python3-the-Hard-Way\src\ex40\ex40a.py
'''
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)