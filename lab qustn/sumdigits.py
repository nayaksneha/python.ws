tnum = num = int(input("enter the number"))
sum = 0
while num >9 :
    sum = (num%10+num//10)
    num = sum
print(num)