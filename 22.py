

name = input("enter name")
lst = ['a','i','o','u','e']
c = 0
for i in name:
    if i in lst:
        c+=1
print(c)