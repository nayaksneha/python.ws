try:
    n1 = int(input("enter the number"))
    n2 = int(input("enter the number"))
    print(n1**n2)
    print(n1/n2)
    print("sum is : "+num1+num2)
except ZeroDivisionError:
    print(f"n2 cant be zeo..")
except ValueError:
    print(f"enter only numbers")
except Exception as e:
    print(f"something went wrng {e}")