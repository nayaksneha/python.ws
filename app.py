from inmmry import Inmmry 

while True:
    print("*"*75)
    print("1.add 2.view 3.update 4.delete 5.search 6.exit")
    print("*"*75)
    ch = int(input("enter choice"))
    if ch == 1:
        Inmmry.addContact() 
    elif ch == 2:
        Inmmry.viewContact()
    elif ch == 3:
        Inmmry.updateContact()
    elif ch == 4:
        Inmmry.deleteContact()
    elif ch == 5:
        Inmmry.searchContact()
    else:
        break

