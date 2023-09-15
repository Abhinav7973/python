row=int(input("enter the number"))
coloumn=row

for i in range(0,row+1):

    for j in range(0,i):
        print("*", end=" ")
    print()