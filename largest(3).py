"""Author:Vijilee
decrioption: Python program to find the largest of three numbers."""
number_1 = int(input("enter number_1"))
number_2 = int(input("enter number_2"))
number_3 = int(input("enter number_3"))
if number_1>number_2 and number_3:
    print("number_1 is greater:", number_1)
elif number_2>number_3 and number_1:
    print("number_2 is greater :",number_2)
elif number_3>number_2 and number_1:
    print("number_3 is greater:",number_3)