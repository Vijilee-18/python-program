def sum(sum_list):
    sum=0
    for i in sum_list:
        sum=sum+i
    return(sum)




sum_list=[]
n=int(input("enter a limit:"))
for i in range(n):
    number=int(input("enter a number:"))
    sum_list.append(number)
a= sum(sum_list)
print(a)
