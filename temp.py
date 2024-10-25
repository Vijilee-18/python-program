"""
author: Vijilee george
description:Python program to convert temperature values back and forth between Celsius and Fahrenheit.
"""
Temp = int(input("enter temperature"))
unit = input("is this in (c)(f)")
if unit == "c":
    f = (9/5*Temp) + 32
    print(Temp,"celsius is",f,)
elif unit =="f":
    c = 5/9*(Temp-32)
    print(Temp,"Fahrenheit is ",c)
