num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))
def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"maximum is {num1}")
    elif num2>num1 and num2>num3:
        print(f"maximum is {num2}")
    else:
        print(f"maximum is {num3}")
maximum(num1,num2,num3)
