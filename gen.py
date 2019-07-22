import random as rn 
gnum = rn.randint(1,6)
print("gnum")
count = 0
while True:
    num = int(input("enter thr number"))
    count += 1
    if num == gnum:

        print(f"you guessed number in {count} attempts")
        break
    elif num < gnum:
        print("guessed num is less the actual number")
        
    else:
        print("guessed num is greater")
        
    if count == 3:
        print("better luck next time")
        break
