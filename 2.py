num = int(input("enter a number"))
temp = num
rev = 0
while num!= 0:
    rev = rev*10 + num%10
    num//=10
print(f"rev of {temp} is {rev}")
