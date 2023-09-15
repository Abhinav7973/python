row=5
col=row
for i in range(row,0,-1):
    print("*", end=" " )


    for j in range(i-1):
        print("*", end=" ")
    print()