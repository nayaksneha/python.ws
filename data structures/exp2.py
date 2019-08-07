try:
    #f = open("data.txt"."w")
    #data = "line one \r\n"
    #f.write(data)
    num = 100/0
except ZeroDivisionError as e:
    print("expect block")
    print(f"{e}")
finally:
    print("finally block")