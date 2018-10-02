# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" Storing variables with .sort function will return NoneType. Ex.: 
    sorted_list = my_list.sort() will return None because it changes variable
    in place. To store in new variable you would do my_list.sort() then
    sorted_list = my_list.sort()

^^^^ This is wrong. Just call my_list.sort() and then my_list will be sorted.
if you want to store a new copy of a sorted list use: sorted(my_list)
