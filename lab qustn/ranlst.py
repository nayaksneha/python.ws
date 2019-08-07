products= {}
while True:
print("1.add 2.display 3.search")
ch = int(input("enter your choice"))
if ch == 1:
    prd_id = int(input("1"))
    prd_name = int(input("abc"))
    products[prd_id]=prd_name
    

elif ch == 2:
    #print(f"the product id and name is :{prd_id} {prd_name}")
    display()

elif ch ==3:
    print(f"enter id: {prd_id}")
    search(prd_id)

