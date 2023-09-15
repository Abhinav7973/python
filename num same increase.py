row=int(input("enter a number"))
col=row
for i in range(0,row):
    for j in range(0,i+1):
        print(j+1, end=" ")
    print()