data = "raj,sneha,sandy,Anu"
print(list(map(lambda x: x.capitalize(),data.split(","))))


x = list(map(lambda x:x.capitalize(),data.split(",")))
print(list(filter(lambda x:x.startswith("A"),x)))