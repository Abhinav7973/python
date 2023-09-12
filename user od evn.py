a=int(input("enter upper limit"))
b=int(input("enter lower limit"))
while a<=b:
    if a%2==0:
        print("even",a)
    else:
        print("odd",a)
    a+=1