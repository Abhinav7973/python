a=int(input("enter the number"))
mul=1
for i in range (a):
 print("multiplication of",i)
 for j in range(10):
   mul=j*i
   print(j,"x",i,"=",mul)