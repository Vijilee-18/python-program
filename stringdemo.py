"""
Author:Vijilee George
18-10-2006
Description: stores a string in a variable. Extract a specific part of the string (substring) and then concatenate it with another string. Finally, display the new string.
"""
str_var = "Hello, World!"
str_another_var = str_var[7:12]
print(str_another_var)
str_var2 = " Everyone!"
str_var3  = str_another_var+str_var2
print(str_var3 )
