def big(n1,n2,n3):
    res = 0
    if num1>num2 and num1>num3:
        res = n1
        
    elif num2>num3:
        res = n2
        
    else:
        res = n3
        return res

num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
num3 = int(input("enter the number"))
print(big(num1,num2,num3))

