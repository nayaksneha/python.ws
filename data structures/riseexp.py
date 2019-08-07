def vote(age):
    assert age >=18, f"age shouldnt be <18 ,it was {age}"
    print("thankyou for voting")

try:
    age = int(input("enter the age"))
    vote(age)
except AssertionError  as a:
    print(a)
else:
    print(f"you entered a valid age:{age}")
finally:
    print("end")