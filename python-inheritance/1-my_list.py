#!/usr/bin/python3
"""module containing class called Mylist"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        number = list(self)
        number = sorted(number)
        print(number)
