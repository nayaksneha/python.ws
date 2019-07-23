name = input("enter name ")
lst = ['a','i','o','u','e','A','E','I','O','U']
print(len(list(filter(lambda x:x in lst,name))))