'''rows=int(input("enter the no of rows:"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print('')
#decreasig triangle
rows =int(input("enter the no. of rows:"))
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print('')'''
#hill pattern
rows=int(input("enter the no.of rows:"))
for i in range(1,rows+1):
    for k in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(" *",end=" ")
    print('')
#reverse hill pattern
rows=int(input("enter the no.of rows:"))
for i in range(rows+1,0,-1):
    for k in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print(" *",end=" ")
    print('')




