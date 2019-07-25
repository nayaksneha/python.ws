'''Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. '''
name = input("enter name")
lst = ['a','i','o','u','e','A','E','I','O','U']

c = list(filter(lambda x: x in lst,name))
print(c)