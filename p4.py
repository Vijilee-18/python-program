def revrsed(str_1):
    reverse=""
    for i in str_1:
        reverse=i+reverse
    return reverse

str_1=input("enter a string:")
print(revrsed(str_1))
