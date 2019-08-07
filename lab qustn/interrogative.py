statement = input("enter the sentence")
#while True:
s = statement.split(" ")
if s[0] in ["does","do","is","are"]:
    print(f"the sentence is interrogative:")
else:
    print(f"the sentence is assertive" )

