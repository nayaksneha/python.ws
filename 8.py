'''Write a program to accept a five-digit number, increment each digit by 1 and then display the new number formed. Note that digit 9 gets incremented to 0.'''
num = int(input("enter the number"))
count = 1
new = 0
while True:
    if num == 0:
        break
    temp = num%10
    num=num//10
    if temp == 9:
        temp=0
        new = new+(temp*count)
        count = count*10
    else:
        temp=temp+1
        new=new+(temp*count)
        count=count*10
print(new)