"""
auhtor :vijilee george 
description:Create, concatenate, and print a string and access a sub-string from a given string.
"""
first_name = input("enter your name :")
last_name = input("enter your last name:")
name = first_name+" "+last_name
print(name)
first_name_length= len(first_name)
sub_string  = name[first_name_length:]
print(sub_string )