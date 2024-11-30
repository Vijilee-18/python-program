def multiply(list):
    x=1
    for i in list:
        x=x*i
    return x
list=[]
n=int(input("enter a limit:"))
for i in range(n):
    x=int(input("enter the number:"))
    list.append(x)

b=multiply(list)
print(b)