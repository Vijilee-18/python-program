'''author:vijilee george
date:21-11-24'''
list_1=[28,13,6]
list_2=[2,34,5,7]
combined_list=list_1+list_2
odd_list=[]
even_list=[]
for i in combined_list:
    if i%2==0:
        odd_list.append(i)
    else:
        even_list.append(i)
odd_list.sort()
even_list.sort()
combined_list.sort()
print(combined_list)
print(odd_list)
print(even_list)
