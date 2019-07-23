lst = []
def add(ele):
    lst.append(ele)
def delete():
    if len(lst) == 0:
        print("lis is empty")
    else:
        ele = lst.pop()
        print(f"element {ele} is removed")

def search(ele):
    if len(lst)== 0:
        print("empty")
    else:
        if ele in lst:
            index = lst.index(ele)
            print(f"element {ele} is found at index {index}")
        else:
            print(f"given {ele} is not found")

    
def display(): 
    if len(lst) == 0:
        print("empty")
    else:
        print(f"list is {lst}")



while True:
    print("\n1.add 2.delete 3.search 4.display 5.exit")
    ch = int(input("enter your choice"))
    if ch == 1:
        ele = int(input("enter the element"))
        add(ele)
    elif ch == 2:
        delete()
    elif ch == 3:
        ele = int(input("enter the element"))
        search(ele)
    elif ch == 4:
        display()
    else:
        print("thankyou")
        break
