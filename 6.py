'''	Write a program to accept a number “n” from the user; then display the sum of the following series:'''

num = int(input("enter the number"))
sum = 0
for i in range(1,num+1):
    sum = sum+ 1/i
print(f"the result is {sum}")