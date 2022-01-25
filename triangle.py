row=int(input("Enter no of rows:"))
for i in range(0,row):
    for j in range(0,i+1):
        print("*",end="")    
    print("")
# *****************************

row=int(input("Enter no of rows:"))
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end="")    
    print("")
# *****************************

row=int(input("Enter no of rows:"))
for i in range(0,row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")    
    print("")
# *****************************

row=int(input("Enter no of rows:"))
for i in range(row,0,-1):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")   
    print("")
    # *****************************

row=int(input("Enter no of rows:"))
for i in range(0,row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,(2*i-1)):
        print("*",end="")   
    print("")
# #     # *****************************

row=int(input("Enter no of rows:"))
for i in range(0,row):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end=" ")   
    print("")
#  *****************************

row=int(input("Enter no of rows:"))
for i in range(row,0,-1):
    for k in range(0,row-i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")   
    print("")


# EASY CODING HERE

n=int(input("Number of rows and col:"))
for i in range(n,0,-1):
    for j in range(0,i-1):
        print(" ",end="")  
    for k in range(0,n-i+1):
        print("*",end=" ")
    print()
# *****************************************************
n=int(input("Number of rows and col:"))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-i):
        print("*",end=" ")
    print()
