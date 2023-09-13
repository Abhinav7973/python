a="malayalam"
rev=""
for i in a:
    print(i)
    rev=i+rev
print(rev)

if rev==a:
    print("String is palindrome")
else:
    print("String is not palindrome")